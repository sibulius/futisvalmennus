"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 18 x 15 m, pikkumaalit porrastettuina noin 3 m kulmista (tuulimylly).
k = Kaavio(18, 15, "Suunnanmuutos porrastettuihin maaleihin 1v1")
for x, y in [(0, 0), (18, 0), (0, 15), (18, 15)]:
    k.cone(x, y, "corner")
k.point_line(0, 0, 18, 15)                            # lävistäjäviiva, jonka yli hyökkääjän on päästävä ennen maalia
# punaisten maalit: yläraja oikealla ja oikea sivu alhaalla
k.goal(12.5, 0, 2.5, vertical=False); k.goal(18, 9.5, 2.5)
# sinisten maalit: vasen sivu ylhäällä ja alaraja vasemmalla
k.goal(0, 3, 2.5); k.goal(3, 15, 2.5, vertical=False)
k.text(13.75, -2.2, "punaisten maali", 10); k.text(18.6, 13.0, "punaisten", 10, anchor="start"); k.text(18.6, 13.8, "maali", 10, anchor="start")
k.text(-2.0, 4.0, "sinisten", 10, anchor="end"); k.text(-2.0, 4.8, "maali", 10, anchor="end"); k.text(4.25, 17.6, "sinisten maali", 10)
k.p(-0.6, 15.9, "A", "H"); k.ball(0.6, 16.4)          # hyökkääjä vasemman alakulman takana
k.p(-2.3, 16.6, "A"); k.p(-3.9, 17.3, "A")            # punaisten jono
k.p(18.6, -0.9, "B", "P")                             # puolustaja oikean yläkulman takana
k.p(20.3, -1.6, "B"); k.p(21.9, -2.3, "B")            # sinisten jono
k.arrow(1.0, 14.0, 6.8, 10.0, "drib")                  # kohti keskikartiota
k.arrow(17.6, 0.8, 12.4, 4.2, "run")                  # puolustaja vastaan
k.arrow(7.2, 9.4, 7.9, 6.0, "drib")                  # näyttää ylärajan maaliin
k.arrow(8.6, 5.4, 14.8, 9.6, "drib")                 # suunnanmuutos oikean sivun maalia kohti
k.arrow(15.3, 10.0, 17.8, 10.8, "shot")               # maali
k.p(11.0, 16.4, "K")                                   # valmentaja sivurajalla
k.dim("18 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punaiset (hyökkäävät)"), ("B", "siniset (puolustavat)"), ("K", "valmentaja"),
        ("point_line", "lävistäjäviiva"), ("drib", "kuljetus"), ("run", "juoksu"), ("shot", "laukaus")],
       png="--png" in sys.argv)
