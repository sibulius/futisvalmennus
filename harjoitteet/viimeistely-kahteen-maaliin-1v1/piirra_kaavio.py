"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Neliö 15 × 15 m: maalit ylä- ja oikealla reunalla, jonot vasemmalla ja alhaalla.
k = Kaavio(15, 15, "Viimeistely kahteen maaliin 1v1")
for x, y in [(0, 0), (15, 0), (0, 15), (15, 15)]:
    k.cone(x, y, "corner")
k.goal(5, 0, 5, vertical=False, big=True)             # yläreunan maali (alajono hyökkää)
k.goal(15, 5, 5, big=True)                            # oikean reunan maali (vasen jono hyökkää)
k.p(7.5, 1.0, "V", "MV"); k.p(14.0, 7.5, "V", "MV")
# vasen jono palloineen: hyökkää oikean reunan maaliin
k.p(1.0, 7.5, "A", "H"); k.ball(2.1, 8.1)
k.queue(-1.4, 7.5, "A", 3, dx=0, dy=1.8)
k.balls(-1.9, 13.2, 2)
# alajono palloineen: hyökkää yläreunan maaliin seuraavaksi
k.queue(7.5, 16.4, "B", 3, dx=1.8)
k.balls(5.0, 16.4, 2)
# puolustaja = edellinen hyökkääjä alajonosta, juuri laukaissut yläreunan maaliin
k.p(8.6, 3.2, "B", "P")
k.arrow(9.2, 4.2, 10.6, 6.6, "run")                   # puolustaja palaa hyökkääjän ja maalin väliin
k.arrow(2.6, 8.2, 7.4, 9.2, "drib")                   # hyökkääjä lähtee omasta aloitteestaan
k.arrow(7.8, 9.6, 11.0, 11.4, "drib")                 # ohitus puolustajan ohi
k.arrow(11.4, 11.0, 14.9, 8.8, "shot")                # laukaus
k.dim("15 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustaja ja toinen jono"), ("V", "maalivahdit"),
        ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
