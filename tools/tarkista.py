#!/usr/bin/env python3
"""Tarkistaa sanasto.yml:n ja kaikkien harjoitteiden frontmatterin.

Käyttö: python tools/tarkista.py
Paluuarvo 0 = kaikki kunnossa, 1 = virheitä.
"""
import copy
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

JUURI = Path(__file__).resolve().parent.parent
virheet: list[str] = []


def virhe(paikka: str, viesti: str) -> None:
    virheet.append(f"{paikka}: {viesti}")


def lue_frontmatter(polku: Path):
    teksti = polku.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", teksti, re.S)
    if not m:
        virhe(str(polku.relative_to(JUURI)), "frontmatter puuttuu (--- ... ---)")
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        virhe(str(polku.relative_to(JUURI)), f"virheellinen YAML: {e}")
        return None


# --- Sanasto ---------------------------------------------------------------
def tarkista_sanasto(s: dict) -> None:
    p = "sanasto.yml"
    alueet = set(s["alueet"])
    kaikki_alavaiheet = {}
    for vk, v in s["vaiheet"].items():
        for ak, a in v["alavaiheet"].items():
            if ak in kaikki_alavaiheet:
                virhe(p, f"alavaihe '{ak}' esiintyy useassa vaiheessa")
            kaikki_alavaiheet[ak] = a or {}
            if a and "alue" in a and a["alue"] not in alueet:
                virhe(p, f"{vk}.{ak}: tuntematon alue '{a['alue']}'")
    for ak, a in kaikki_alavaiheet.items():
        vp = a.get("vastinpari")
        if vp is None:
            continue
        if vp not in kaikki_alavaiheet:
            virhe(p, f"{ak}: tuntematon vastinpari '{vp}'")
        elif kaikki_alavaiheet[vp].get("vastinpari") != ak:
            virhe(p, f"{ak} ↔ {vp}: vastinpari ei ole molemminpuolinen")


# --- Harjoite --------------------------------------------------------------
def rakenna_skeema(s: dict) -> dict:
    with open(JUURI / "schema" / "harjoite.schema.json", encoding="utf-8") as f:
        sk = json.load(f)
    sk = copy.deepcopy(sk)
    pr = sk["properties"]
    roolit = [r for ryhma in s["pelin_keskus"]["roolit"].values() for r in ryhma]
    vakio = s["vaiheet"].get("vakiotilanne", {})
    pr["vaihe"]["enum"] = list(s["vaiheet"])
    pr["alavaihe"]["enum"] = [a for v in s["vaiheet"].values() for a in v["alavaiheet"]]
    pr["myos_alavaiheet"]["items"]["enum"] = pr["alavaihe"]["enum"]
    pr["alue"]["enum"] = list(s["alueet"])
    pr["kaistat"]["items"]["enum"] = list(s.get("kaistat", {}))
    pk = pr["pelin_keskus"]["properties"]
    pk["tilanne"]["enum"] = s["pelin_keskus"]["tilanteet"]
    pk["roolit"]["items"]["enum"] = roolit
    pk["vastaroolit"]["items"]["enum"] = roolit
    pr["paineistaminen"]["enum"] = list(s["paineistaminen"])
    pr["puoli"]["enum"] = vakio.get("puolet", [])
    pr["tehtavat"]["items"]["enum"] = vakio.get("tehtavat", [])
    return sk


def tarkista_harjoite(polku: Path, fm: dict, s: dict, validoija) -> None:
    p = str(polku.relative_to(JUURI))
    for e in sorted(validoija.iter_errors(fm), key=lambda e: list(e.path)):
        kentta = ".".join(str(x) for x in e.path) or "(juuri)"
        virhe(p, f"{kentta}: {e.message}")

    kansio = polku.parent.name
    if not kansio.startswith("_") and fm.get("tunniste") != kansio:
        virhe(p, f"tunniste '{fm.get('tunniste')}' ≠ kansion nimi '{kansio}'")

    vaihe = s["vaiheet"].get(fm.get("vaihe"))
    if not vaihe:
        return
    if fm.get("alavaihe") not in vaihe["alavaiheet"]:
        virhe(p, f"alavaihe '{fm.get('alavaihe')}' ei kuulu vaiheeseen '{fm.get('vaihe')}'")
    if fm.get("alavaihe") in (fm.get("myos_alavaiheet") or []):
        virhe(p, "myos_alavaiheet ei saa sisältää pääalavaihetta")

    on_vakio = fm.get("vaihe") == "vakiotilanne"
    if on_vakio and "puoli" not in fm:
        virhe(p, "vakiotilanteessa 'puoli' on pakollinen")
    if not on_vakio:
        for k in ("puoli", "tehtavat"):
            if k in fm:
                virhe(p, f"'{k}' on sallittu vain vakiotilanteissa")
        if "pelin_keskus" not in fm and fm.get("vaihe") != "tekniikka":
            virhe(p, "'pelin_keskus' on pakollinen muissa kuin vakiotilanteissa ja tekniikkaharjoitteissa")

    pk = fm.get("pelin_keskus")
    if not isinstance(pk, dict):
        return
    sallitut = set(vaihe.get("sallitut_roolit") or [])
    roolit = pk.get("roolit") or []
    if sallitut:
        for r in roolit:
            if r not in sallitut:
                virhe(p, f"rooli '{r}' ei ole sallittu vaiheessa '{fm['vaihe']}'")
    if fm.get("paineistaminen") == "ei" and pk.get("vastaroolit"):
        virhe(p, "paineistaminen 'ei', mutta vastarooleja on merkitty")
    m = re.match(r"^(\d)v(\d)$", str(pk.get("tilanne", "")))
    if m:
        hyok, puol = int(m.group(1)), int(m.group(2))
        kaikki = roolit + (pk.get("vastaroolit") or [])
        h = [r for r in kaikki if r.endswith("H")]
        pp = [r for r in kaikki if r.endswith("P")]
        if len(h) > hyok:
            virhe(p, f"tilanne {pk['tilanne']}: hyökkääjärooleja {len(h)} > {hyok}")
        if len(pp) > puol:
            virhe(p, f"tilanne {pk['tilanne']}: puolustajarooleja {len(pp)} > {puol}")


def main() -> int:
    with open(JUURI / "sanasto.yml", encoding="utf-8") as f:
        s = yaml.safe_load(f)
    tarkista_sanasto(s)
    validoija = Draft202012Validator(rakenna_skeema(s))
    tiedostot = sorted((JUURI / "harjoitteet").glob("*/harjoite.md"))
    for polku in tiedostot:
        fm = lue_frontmatter(polku)
        if fm is not None:
            tarkista_harjoite(polku, fm, s, validoija)
    if virheet:
        print(f"❌ {len(virheet)} virhettä:")
        for v in virheet:
            print(f"  - {v}")
        return 1
    print(f"✅ Sanasto ja {len(tiedostot)} harjoitetta kunnossa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
