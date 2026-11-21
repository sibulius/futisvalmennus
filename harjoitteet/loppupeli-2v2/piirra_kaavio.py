"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(25, 18, "Loppupeli 2v2")
for x, y in [(0, 0), (25, 0), (0, 18), (25, 18)]:
    k.cone(x, y, "corner")
k.line(12.5, 0, 12.5, 18, dashed=True)             # keskiviiva
k.goal(0, 6.5, 5, big=True); k.goal(25, 6.5, 5, big=True)
k.p(1.0, 9, "V", "MV"); k.p(24.0, 9, "V", "MV")
# punainen hyökkää oikealle
k.p(9.0, 10.0, "A", "1H"); k.ball(9.9, 10.6)
k.p(15.5, 4.2, "A", "2H")
# sininen puolustaa
k.p(11.3, 11.8, "B", "1P")
k.p(16.6, 7.8, "B", "2P")
k.arrow(18.0, 6.8, 16.2, 5.0, "run")       # 2H vapautuu 2P:n varjosta
k.arrow(10.0, 9.6, 14.8, 4.8, "pass")      # 1H -> 2H
k.arrow(16.3, 4.0, 19.4, 5.4, "drib")      # ensimmäinen kosketus eteenpäin
k.arrow(20.0, 5.8, 24.6, 7.1, "shot")      # laukaus
k.p(11.5, 19.6, "K", "V"); k.balls(13.1, 19.6, 3)
# vaihtopelaajat sivurajan takana
k.p(4.5, 19.6, "A"); k.p(19.0, 19.6, "B")
k.text(5.6, 19.8, "vaihdossa", 10, anchor="start"); k.text(20.1, 19.8, "vaihdossa", 10, anchor="start")
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahdit"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("shot", "laukaus"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
