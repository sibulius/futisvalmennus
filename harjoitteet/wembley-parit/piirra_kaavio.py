"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio, TEAM  # noqa: E402

# jokaisella parilla oma väri
TEAM["D"] = ("#f97316", "#7c2d12")   # oranssi
TEAM["E"] = ("#8b5cf6", "#4c1d95")   # violetti

# Pituus 30 m, leveys 20 m; hyökkäys oikealle (vasen = ylhäällä).
k = Kaavio(30, 20, "Wembley-parit")
for x, y in [(0, 0), (30, 0), (0, 20), (30, 20)]:
    k.cone(x, y, "corner")
k.goal(30, 7.5, 5, big=True)
k.p(29.0, 10.0, "V", "MV")
# valmentaja ja pallovarasto maalia vastapäätä
k.p(-1.6, 10.0, "K", "V"); k.balls(-2.6, 12.0, 3)
# pari 1 (punainen) hyökkää pallon kanssa
k.p(15.5, 8.0, "A", "1H"); k.ball(16.5, 8.6)
k.p(19.0, 14.5, "A", "2H")
# muut parit puolustavat, lähin pari (sininen) 1P ja 2P
k.p(19.5, 6.0, "B", "1P"); k.p(13.0, 12.5, "B", "2P")
k.p(22.5, 11.5, "D"); k.p(10.5, 5.0, "D")
k.p(7.0, 14.0, "E"); k.p(24.0, 4.0, "E")
# jatkoon päässyt pari odottaa sivussa
k.p(4.0, -1.8, "C"); k.p(6.0, -1.8, "C")
k.arrow(17.0, 9.0, 21.0, 8.6, "drib")       # 1H kuljettaa ruuhkan ohi
k.arrow(21.6, 8.6, 29.6, 9.0, "shot")       # ja laukoo
k.arrow(19.6, 14.0, 24.6, 12.8, "run")      # 2H seuraa toisen pallon varalle
k.arrow(19.8, 6.8, 20.6, 8.0, "run")        # 1P painostaa
k.dim("30 m", "20 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pari 1 (pallollinen)"), ("B", "pari 2"), ("D", "pari 3"), ("E", "pari 4"),
        ("C", "pari 5 (jatkossa)"),
        ("V", "maalivahti"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
