"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio, CONE  # noqa: E402

# Ylös nostetut värikartiot (merkit) omina symboleinaan.
CONE["punainen"] = ("#dc2626", "#7f1d1d", "punainen merkki")
CONE["vihrea"] = ("#22c55e", "#14532d", "vihreä merkki")

k = Kaavio(10, 10, "Havainnointi värikartioilla", scale=1.4)
for x, y in [(0, 0), (10, 0), (0, 10), (10, 10)]:
    k.cone(x, y, "corner")
# ulkopelaajat sivujen keskellä; pallo alasivun pelaajalla
k.p(5, -1.2, "C"); k.cone(6.2, -1.9, "punainen")
k.p(-1.2, 5, "C"); k.cone(-2.3, 3.9, "punainen")
k.p(11.2, 5, "C"); k.cone(12.3, 3.9, "vihrea")
k.p(5, 11.2, "C"); k.ball(6.1, 11.6)
k.p(5, 5, "A")                                         # keskipelaaja
k.arrow(5, 10.3, 5, 5.9, "pass")                       # syöttö keskipelaajalle
k.arrow(5.8, 5, 10.2, 5, "pass")                       # kaksi punaista, yksi vihreä → vihreälle
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("C", "ulkopelaajat"), ("A", "keskipelaaja"), ("pass", "syöttö")],
       png="--png" in sys.argv)
