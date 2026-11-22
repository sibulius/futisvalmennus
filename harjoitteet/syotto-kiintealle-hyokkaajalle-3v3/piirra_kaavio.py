"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(25, 20, "Syöttö kiinteälle hyökkääjälle 3v3")
k.zone(0, 0, 4, 20, dashed=True); k.zone(21, 0, 4, 20, dashed=True)
for x, y in [(0, 0), (25, 0), (0, 20), (25, 20), (4, 0), (4, 20), (21, 0), (21, 20)]:
    k.cone(x, y, "corner")
k.text(2, 1.6, "maalialue", 9); k.text(23, 1.4, "maalinteko-", 9); k.text(23, 2.2, "vyöhyke", 9)
for x in (0, 25):
    k.goal(x, 3, 2.5); k.goal(x, 14.5, 2.5)
# punainen hyökkää oikealle, kiinteä hyökkääjä vastustajan maalialueella
k.p(6.0, 9.0, "A", "1H"); k.ball(6.9, 9.6)
k.p(10.0, 3.5, "A", "2H")
k.p(10.5, 15.5, "A", "3H")
k.p(22.6, 12.0, "A", "KH")
# sininen puolustaa, oma kiinteä hyökkääjä punaisen maalialueella
k.p(9.0, 8.0, "B", "1P")
k.p(14.5, 6.5, "B", "2P")
k.p(15.5, 12.5, "B", "3P")
k.p(2.4, 6.0, "B", "KH")
k.arrow(7.3, 9.8, 21.7, 11.8, "pass")    # 1H -> KH linjojen läpi
k.arrow(11.0, 3.4, 18.5, 4.6, "run")     # 2H seuraa tueksi
k.arrow(22.9, 12.9, 24.2, 15.0, "shot")  # KH viimeistelee
k.p(10.5, 21.6, "K", "V"); k.balls(12.1, 21.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("shot", "laukaus"), ("run", "liike")],
       png="--png" in sys.argv)
