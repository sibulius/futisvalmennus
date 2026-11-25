"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 15, "Päätypeli 3v3+2")
for x, y in [(0, 0), (20, 0), (0, 15), (20, 15)]:
    k.cone(x, y, "corner")
# päätypelaajat (pelaavat pallollisen kanssa)
k.p(-1.4, 7.5, "C"); k.p(21.4, 7.5, "C")
# hyökkäävä joukkue
k.p(5.0, 3.2, "A", "2H")
k.p(10.5, 9.0, "A", "1H")
k.p(6.0, 12.5, "A", "3H")
# puolustava joukkue
k.p(8.0, 5.0, "B", "1P")
k.p(12.5, 6.2, "B", "2P")
k.p(14.0, 11.0, "B", "3P")
k.ball(-0.4, 8.6)
k.arrow(-0.6, 8.2, 4.6, 3.9, "pass")       # päätypelaaja -> 2H
k.arrow(5.6, 3.8, 10.0, 8.4, "pass")       # 2H -> 1H
k.arrow(11.2, 9.2, 14.4, 8.6, "drib")   # 1H kuljettaa tilaan
k.arrow(14.8, 8.4, 20.6, 7.6, "pass")      # 1H -> vastakkainen päätypelaaja
k.arrow(8.0, 5.6, 9.6, 8.0, "run")         # 1P painostaa
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkää"), ("B", "puolustaa"), ("C", "päätypelaaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")], png="--png" in sys.argv)
