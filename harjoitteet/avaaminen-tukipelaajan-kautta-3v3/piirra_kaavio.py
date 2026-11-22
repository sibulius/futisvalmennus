"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(25, 20, "Avaaminen tukipelaajan kautta 3v3")
k.zone(0, 0, 4, 20, dashed=True); k.zone(21, 0, 4, 20, dashed=True)
for x, y in [(0, 0), (25, 0), (0, 20), (25, 20), (4, 0), (4, 20), (21, 0), (21, 20)]:
    k.cone(x, y, "corner")
k.text(2, 1.6, "maalialue", 9); k.text(23, 1.4, "maalinteko-", 9); k.text(23, 2.2, "vyöhyke", 9)
for x in (0, 25):
    k.goal(x, 3, 2.5); k.goal(x, 14.5, 2.5)
# punainen hyökkää oikealle, tukipelaaja oman maalinsa edessä
k.p(2.2, 10, "A", "TP")
k.p(9.5, 5.5, "A", "1H")
k.p(12.5, 9.5, "A", "2H")
k.p(10.5, 16.5, "A", "3H")
# sininen puolustaa, oma tukipelaaja oikeassa maalialueessa
k.p(11.0, 4.3, "B", "1P")
k.p(13.8, 8.4, "B", "2P")
k.p(15.5, 13.0, "B", "3P")
k.p(22.8, 10, "B", "TP")
k.arrow(9.0, 6.2, 3.2, 9.4, "pass")      # 1H -> TP taakse
k.arrow(3.1, 10.8, 9.6, 16.0, "pass")    # TP kääntää pelin vapaalle puolelle
k.ball(3.0, 10.0)
k.arrow(11.4, 16.6, 16.0, 17.0, "drib")  # 3H vie pallon eteenpäin
k.arrow(9.5, 6.4, 8.6, 9.6, "run")       # 1H uuteen syöttökulmaan
k.p(10.5, 21.6, "K", "V"); k.balls(12.1, 21.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
