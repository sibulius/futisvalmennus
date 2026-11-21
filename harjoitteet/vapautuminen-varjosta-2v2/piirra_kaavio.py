"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(15, 15, "Vapautuminen varjosta 2v2")
for x, y in [(0, 0), (15, 0), (0, 15), (15, 15)]:
    k.cone(x, y, "corner")
# joukkue 1 (punainen) päätypelaajat: vasen ja oikea sivu
k.p(-1.4, 6.3, "A"); k.p(16.4, 6.3, "A")
# joukkue 2 (sininen) päätypelaajat: ylä- ja alasivu
k.p(7.5, -1.4, "B"); k.p(7.5, 16.4, "B")
# keskellä 2v2
k.p(4.2, 6.6, "B", "1P")
k.p(10.4, 8.4, "B", "2P")
k.p(6.8, 3.8, "A", "1H")
k.p(9.6, 11.6, "A", "2H")
k.arrow(6.4, 6.9, 6.75, 4.9, "run")      # 1H irtautuu varjosta
k.arrow(-0.6, 6.2, 5.9, 4.2, "pass")     # päätypelaaja -> 1H
k.ball(7.7, 4.4)
k.arrow(8.0, 4.0, 15.5, 6.2, "pass")     # 1H -> vastakkainen päätypelaaja
# valmentaja ja pallot
k.p(11.5, 16.8, "K", "V"); k.balls(13.1, 16.8, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "joukkue 1 – hyökkää"), ("B", "joukkue 2 – puolustaa"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("run", "liike")], png="--png" in sys.argv)
