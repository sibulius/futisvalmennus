"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 15, "Avaaminen tukipelaajan kautta 2v2")
k.zone(0, 0, 3, 15, dashed=True); k.zone(17, 0, 3, 15, dashed=True)
for x, y in [(0, 0), (20, 0), (0, 15), (20, 15), (3, 0), (3, 15), (17, 0), (17, 15)]:
    k.cone(x, y, "corner")
k.text(1.5, 1.3, "maalialue", 8); k.text(18.5, 1.1, "maalinteko-", 8); k.text(18.5, 1.8, "vyöhyke", 8)
for x in (0, 20):
    k.goal(x, 2, 2); k.goal(x, 11, 2)
# punainen hyökkää oikealle, tukipelaaja oman maalinsa edessä
k.p(1.6, 7.5, "A", "TP")
k.p(7.5, 4.0, "A", "1H")
k.p(8.0, 12.0, "A", "2H")
# sininen puolustaa
k.p(8.8, 3.0, "B", "1P")
k.p(11.0, 8.0, "B", "2P")
k.p(18.4, 7.5, "B", "TP")
k.arrow(7.0, 4.6, 2.4, 7.0, "pass")      # 1H -> TP taakse
k.arrow(2.3, 8.2, 7.2, 11.6, "pass")     # TP kääntää pelin
k.ball(2.4, 7.5)
k.arrow(8.9, 12.1, 13.0, 12.5, "drib")   # 2H vie pallon eteenpäin
k.arrow(7.6, 4.8, 9.6, 7.8, "run")       # 1H uuteen syöttökulmaan
k.p(8.5, 16.6, "K", "V"); k.balls(10.1, 16.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
