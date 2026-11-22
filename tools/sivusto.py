#!/usr/bin/env python3
"""Generoi harjoitepankin verkkosivun (GitHub Pages) kansioon _site/.

Käyttö:
    python tools/sivusto.py            # build → _site/
    python tools/sivusto.py --serve    # build ja paikallinen palvelin (http://localhost:8000)

Riippuvuudet: pip install pyyaml markdown jinja2

Tietosuoja: sivulle julkaistaan VAIN sallitut tiedostot (SALLITUT) kansioista
harjoitteet/<tunniste>/ sekä sanasto.yml:n sisältö. Kansiot, joiden nimi alkaa
alaviivalla (esim. _malli), ohitetaan.
"""
import json
import os
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

JUURI = Path(__file__).resolve().parent.parent
LAHDE = JUURI / "sivusto"
KOHDE = JUURI / "_site"
REPO = os.environ.get("GITHUB_REPOSITORY", "sibulius/futisvalmennus")
HAARA = "main"

# Ainoat harjoitekansioista julkaistavat tiedostot.
SALLITUT = ("harjoite.md", "variaatiot.md", "kaavio.svg")


# --- Lukeminen -------------------------------------------------------------
def jaa_frontmatter(teksti: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", teksti, re.S)
    if not m:
        raise ValueError("frontmatter puuttuu")
    return yaml.safe_load(m.group(1)) or {}, teksti[m.end():]


def md_html(teksti: str) -> str:
    # GitHub hyväksyy listan heti kappaleen perään ilman tyhjää riviä,
    # Python-Markdown ei: lisätään tyhjä rivi, jotta tulos vastaa GitHubia.
    teksti = re.sub(r"^([^\s\-*\d#>|][^\n]*)\n(?=(?:[-*] |\d+\. ))", r"\1\n\n", teksti, flags=re.M)
    return markdown.markdown(teksti, extensions=["extra", "sane_lists"])


def poista_h1(teksti: str) -> str:
    """Poistaa ensimmäisen # -otsikon (otsikko näytetään pohjassa)."""
    return re.sub(r"^\s*# [^\n]*\n", "", teksti, count=1)


def lue_harjoitteet(s: dict) -> list[dict]:
    harjoitteet = []
    for kansio in sorted((JUURI / "harjoitteet").iterdir()):
        if not kansio.is_dir() or kansio.name.startswith("_"):
            continue
        polku = kansio / "harjoite.md"
        if not polku.exists():
            continue
        fm, runko = jaa_frontmatter(polku.read_text(encoding="utf-8"))
        if fm.get("tunniste") != kansio.name:
            raise ValueError(f"{polku}: tunniste ei vastaa kansion nimeä")
        variaatiot = ""
        vp = kansio / "variaatiot.md"
        if vp.exists():
            # Variaatiot sivun alaosioksi: h1 pois, otsikot tasoa alemmas.
            v = poista_h1(vp.read_text(encoding="utf-8"))
            v = re.sub(r"^(#{2,5}) ", r"#\1 ", v, flags=re.M)
            variaatiot = md_html(v)
        harjoitteet.append({
            **fm,
            "kansio": kansio,
            "runko_html": md_html(poista_h1(runko)),
            "variaatiot_html": variaatiot,
            "kaavio": (kansio / "kaavio.svg").exists(),
        })
    return harjoitteet


# --- Sanaston nimet --------------------------------------------------------
class Sanasto:
    def __init__(self, s: dict):
        self.s = s
        self.vaiheet = s["vaiheet"]
        self.alavaiheet = {}            # avain -> (vaihe, tiedot)
        for va, vt in self.vaiheet.items():
            for aa, at in vt["alavaiheet"].items():
                self.alavaiheet[aa] = (va, at)
        r = s["pelin_keskus"]["roolit"]
        self.roolit = {**r["hyokkaaminen"], **r["puolustaminen"]}

    def vaihe(self, k):
        return self.vaiheet[k]["nimi"]

    def alavaihe(self, k):
        return self.alavaiheet[k][1]["nimi"]

    def alue(self, k):
        return self.s["alueet"][k]

    def kaista(self, k):
        return self.s["kaistat"][k]["nimi"]

    def kaista_lyh(self, k):
        return self.s["kaistat"][k]["lyhenne"]

    def paine(self, k):
        return k.capitalize() if k != "ei" else "Ei paineistusta"

    def vastinpari(self, alavaihe):
        return self.alavaiheet[alavaihe][1].get("vastinpari")


def ika_jarjestys(ika: str) -> int:
    return int(ika[1:])


# --- Generointi ------------------------------------------------------------
def rakenna() -> int:
    with open(JUURI / "sanasto.yml", encoding="utf-8") as f:
        s = yaml.safe_load(f)
    sn = Sanasto(s)
    harjoitteet = lue_harjoitteet(s)

    if KOHDE.exists():
        shutil.rmtree(KOHDE)
    KOHDE.mkdir()
    shutil.copytree(LAHDE / "staattinen", KOHDE / "staattinen")
    (KOHDE / ".nojekyll").write_text("")

    env = Environment(
        loader=FileSystemLoader(LAHDE / "pohjat"),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    yhteiset = {"sn": sn, "repo": REPO, "haara": HAARA}

    # Suodatinvalinnat: vain arvot, joita harjoitteissa oikeasti on, sanaston järjestyksessä.
    kaytetyt = lambda kentta: {x for h in harjoitteet for x in (
        h.get(kentta) if isinstance(h.get(kentta), list) else [h.get(kentta)]) if x}
    tilanteet = {h["pelin_keskus"]["tilanne"] for h in harjoitteet if h.get("pelin_keskus")}
    roolit = {r for h in harjoitteet if h.get("pelin_keskus")
              for r in h["pelin_keskus"]["roolit"] + (h["pelin_keskus"].get("vastaroolit") or [])}
    suodattimet = {
        "vaiheet": [(k, v["nimi"], [(a, at["nimi"]) for a, at in v["alavaiheet"].items()
                                     if a in kaytetyt("alavaihe")])
                    for k, v in sn.vaiheet.items() if k in kaytetyt("vaihe")],
        "alueet": [(k, v) for k, v in s["alueet"].items() if k in kaytetyt("alue")],
        "tilanteet": [t for t in s["pelin_keskus"]["tilanteet"] if t in tilanteet],
        "roolit": [r for r in sn.roolit if r in roolit],
        "paineet": [(k, sn.paine(k)) for k in s["paineistaminen"] if k in kaytetyt("paineistaminen")],
        "iat": sorted(kaytetyt("ika"), key=ika_jarjestys),
        "kaistat": [(k, v["nimi"]) for k, v in s["kaistat"].items() if k in kaytetyt("kaistat")],
    }

    # Etusivu
    (KOHDE / "index.html").write_text(env.get_template("etusivu.html").render(
        **yhteiset, juuri="", harjoitteet=harjoitteet, suodattimet=suodattimet,
        otsikko="Harjoitteet"), encoding="utf-8")

    # Sanasto
    (KOHDE / "sanasto").mkdir()
    (KOHDE / "sanasto" / "index.html").write_text(env.get_template("sanasto.html").render(
        **yhteiset, juuri="../", s=s, otsikko="Sanasto"), encoding="utf-8")

    # Harjoitesivut
    pohja = env.get_template("harjoite.html")
    for h in harjoitteet:
        kohde = KOHDE / "harjoitteet" / h["tunniste"]
        kohde.mkdir(parents=True)
        if h["kaavio"]:
            shutil.copy2(h["kansio"] / "kaavio.svg", kohde / "kaavio.svg")
        vp = sn.vastinpari(h["alavaihe"])
        vastinparin = [x for x in harjoitteet if vp and x["alavaihe"] == vp]
        (kohde / "index.html").write_text(pohja.render(
            **yhteiset, juuri="../../", h=h, vastinpari=vp, vastinparin=vastinparin,
            otsikko=h["nimi"]), encoding="utf-8")

    # Koneluettava hakemisto muille työkaluille.
    hakemisto = [{k: v for k, v in h.items() if k not in ("kansio", "runko_html", "variaatiot_html")}
                 | {"osoite": f"harjoitteet/{h['tunniste']}/"} for h in harjoitteet]
    (KOHDE / "harjoitteet.json").write_text(
        json.dumps(hakemisto, ensure_ascii=False, indent=1), encoding="utf-8")

    # Tietosuojavarmistus: sivustolle ei saa päätyä muita tiedostoja harjoitekansioista.
    for p in (KOHDE / "harjoitteet").rglob("*"):
        if p.is_file() and p.name not in ("index.html", "kaavio.svg"):
            raise RuntimeError(f"Odottamaton tiedosto sivustolla: {p}")

    print(f"✅ Sivusto rakennettu: {KOHDE.relative_to(JUURI)}/ ({len(harjoitteet)} harjoitetta)")
    return 0


def palvele() -> None:
    import functools
    import http.server
    kasittelija = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(KOHDE))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 8000), kasittelija) as srv:
        print("Palvelin: http://localhost:8000 (Ctrl+C lopettaa)")
        srv.serve_forever()


if __name__ == "__main__":
    tulos = rakenna()
    if "--serve" in sys.argv:
        palvele()
    sys.exit(tulos)
