"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 15, "Syöttö kiinteälle hyökkääjälle 2v2")
k.zone(0, 0, 3, 15, dashed=True); k.zone(17, 0, 3, 15, dashed=True)
for x, y in [(0, 0), (20, 0), (0, 15), (20, 15), (3, 0), (3, 15), (17, 0), (17, 15)]:
    k.cone(x, y, "corner")
k.text(1.5, 1.3, "maalialue", 8); k.text(18.5, 1.1, "maalinteko-", 8); k.text(18.5, 1.8, "vyöhyke", 8)
for x in (0, 20):
    k.goal(x, 2, 2); k.goal(x, 11, 2)
# punainen hyökkää oikealle, kiinteä hyökkääjä vastustajan maalialueella
k.p(5.0, 7.0, "A", "1H"); k.ball(5.9, 7.6)
k.p(8.0, 12.0, "A", "2H")
k.p(18.2, 9.0, "A", "KH")
# sininen puolustaa, oma kiinteä hyökkääjä punaisen maalialueella
k.p(7.4, 6.2, "B", "1P")
k.p(11.5, 9.5, "B", "2P")
k.p(1.8, 4.5, "B", "KH")
k.arrow(6.2, 7.6, 17.3, 8.8, "pass")     # 1H -> KH
k.arrow(8.8, 11.6, 14.6, 10.4, "run")    # 2H seuraa tueksi
k.arrow(18.4, 9.9, 19.4, 11.6, "shot")   # KH viimeistelee
k.p(8.5, 16.6, "K", "V"); k.balls(10.1, 16.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("shot", "laukaus"), ("run", "liike")],
       png="--png" in sys.argv)
