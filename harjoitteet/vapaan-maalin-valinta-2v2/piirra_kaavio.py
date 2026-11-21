"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 16, "Vapaan maalin valinta 2v2")
for x, y in [(0, 0), (20, 0), (0, 16), (20, 16)]:
    k.cone(x, y, "corner")
# laukaisualueet 4 m päätyrajoista
k.line(4, 0, 4, 16); k.line(16, 0, 16, 16)
for x in (4, 16):
    k.cone(x, 0, "line"); k.cone(x, 16, "line")
k.text(2, 8.2, "laukaisu-", 10); k.text(2, 9.0, "alue", 10)
k.text(18, 8.2, "laukaisu-", 10); k.text(18, 9.0, "alue", 10)
# kaksi pikkumaalia kummassakin päädyssä
k.goal(0, 1.5, 2); k.goal(0, 12.5, 2)
k.goal(20, 1.5, 2); k.goal(20, 12.5, 2)
# odottavat parit omien maaliensa takana
k.queue(-1.6, 7.1, "A", 2, dx=0, dy=1.8)
k.queue(21.6, 7.1, "B", 2, dx=0, dy=1.8)
# kentällä 2v2: punainen hyökkää oikealle
k.p(7.0, 11.0, "A", "1H"); k.ball(7.9, 11.6)
k.p(9.6, 12.2, "B", "1P")
k.p(12.2, 8.3, "B", "2P")
k.p(14.4, 7.9, "A", "2H")
k.arrow(14.2, 7.0, 13.7, 4.6, "run")      # 2H vapautuu 2P:n varjosta
k.arrow(7.9, 10.8, 13.1, 4.2, "pass")     # 1H -> 2H
k.arrow(14.3, 3.6, 16.8, 2.8, "drib")     # ensimmäinen kosketus kohti vapaata maalia
k.arrow(17.2, 2.6, 19.6, 2.5, "shot")     # laukaus laukaisualueelta
# valmentaja ja pallot
k.p(8.5, 17.4, "K", "V"); k.balls(10.1, 17.4, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("shot", "laukaus"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
