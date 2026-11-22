"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio, CONE  # noqa: E402

CONE["kierto"] = ("#f97316", "#7c2d12", "kierrettävä kartio")

# Pituus 24 m, leveys 20 m; hyökkäys oikealle (vasen = ylhäällä).
k = Kaavio(24, 20, "Viimeistely paineessa 1v1")
k.goal(24, 7.5, 5, big=True)
k.p(23.0, 10.0, "V", "MV")
# jonot lähtöpäädyssä: puolustajat vasemmalla palloineen, hyökkääjät oikealla
k.p(2.0, 4.0, "B", "P"); k.ball(3.0, 4.9)
k.p(0.2, 2.4, "B"); k.p(-1.6, 0.8, "B")
k.balls(-2.6, 3.2, 2)
k.p(2.0, 16.0, "A", "H")
k.p(0.2, 17.6, "A"); k.p(-1.6, 19.2, "A")
# kierrettävät kartiot jonojen edessä
k.cone(6.0, 5.5, "kierto"); k.cone(6.0, 14.5, "kierto")
k.arrow(3.2, 5.6, 3.2, 15.0, "pass")                  # poikittaissyöttö hyökkääjälle
k.arrow(2.8, 3.2, 7.0, 4.2, "run")                    # puolustaja kiertää kartion ulkokautta
k.arrow(7.2, 4.6, 13.0, 9.4, "run")                   # ja painostaa
k.arrow(3.4, 16.6, 7.2, 16.2, "drib")                 # hyökkääjä kuljettaa kartion ulkokautta
k.arrow(7.4, 15.8, 14.4, 11.6, "drib")                # kohti maalia
k.arrow(15.0, 11.2, 23.8, 11.8, "shot")               # laukaus
k.dim("24 m", "20 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahti"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
