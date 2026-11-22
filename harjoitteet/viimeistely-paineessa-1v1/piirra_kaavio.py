"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio, CONE  # noqa: E402

CONE["kierto"] = ("#f97316", "#7c2d12", "kierrettävä kartio")

# Pituus 20 m, leveys 15 m; hyökkäys oikealle (vasen = ylhäällä).
k = Kaavio(20, 15, "Viimeistely paineessa 1v1")
k.goal(20, 5, 5, big=True)
k.p(19.0, 7.5, "V", "MV")
# jonot lähtöpäädyssä: puolustajat vasemmalla palloineen, hyökkääjät oikealla
k.p(1.6, 3.0, "B", "P"); k.ball(2.6, 3.8)
k.p(-0.2, 1.6, "B"); k.p(-2.0, 0.2, "B")
k.balls(-2.8, 2.6, 2)
k.p(1.6, 12.0, "A", "H")
k.p(-0.2, 13.4, "A"); k.p(-2.0, 14.8, "A")
# kierrettävät kartiot jonojen edessä
k.cone(4.5, 5.0, "kierto"); k.cone(4.5, 10.0, "kierto")
k.arrow(2.6, 4.6, 2.6, 11.0, "pass")                  # poikittaissyöttö hyökkääjälle
k.arrow(2.8, 2.8, 5.4, 3.6, "run")                    # puolustaja kiertää kartion ulkokautta
k.arrow(5.8, 4.6, 10.6, 7.0, "run")                   # ja painostaa
k.arrow(2.8, 12.4, 5.2, 11.6, "drib")                 # hyökkääjä kuljettaa kartion ulkokautta
k.arrow(5.6, 11.0, 11.4, 8.6, "drib")                # kohti maalia
k.arrow(12.0, 8.4, 19.8, 8.9, "shot")               # laukaus
k.line(4.5, 5.6, 4.5, 9.4, dashed=True, width=1)
k.text(5.4, 7.7, "5 m", 11)
k.dim("20 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahti"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
