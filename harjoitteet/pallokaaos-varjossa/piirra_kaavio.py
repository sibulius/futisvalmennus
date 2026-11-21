"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 20, "Pallokaaos varjossa")
for x, y in [(0, 0), (20, 0), (0, 20), (20, 20)]:
    k.cone(x, y, "corner")
# pari 1: 1H ja 2H
k.p(4.5, 14.5, "A", "1H"); k.ball(5.4, 15.0)
k.p(13.8, 14.4, "A", "2H")
# pari 2
k.p(4.0, 4.0, "A"); k.ball(4.9, 4.4)
k.p(15.5, 2.8, "A")
# puolustajat kuljettavat omaa palloaan
k.p(8.8, 12.0, "B", "1P"); k.ball(9.6, 12.6)
k.p(15.0, 6.6, "B", "2P"); k.ball(15.8, 7.1)
k.p(16.8, 17.6, "B"); k.ball(17.7, 18.0)
k.p(3.0, 9.0, "B"); k.ball(3.9, 9.4)
k.arrow(12.6, 10.4, 13.5, 13.2, "run")      # 2H vapautuu 1P:n varjosta
k.arrow(6.0, 14.6, 12.6, 14.4, "pass")      # 1H -> 2H
k.arrow(14.4, 5.9, 11.6, 4.3, "drib")       # 2P kuljettaa pari 2:n syöttölinjalle
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat (kuljettavat palloa)"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
