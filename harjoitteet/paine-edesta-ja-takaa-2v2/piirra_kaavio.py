"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 25 m (iso maali vasemmalla, pikkumaalit oikealla), leveys 18 m; hyökkäys oikealle.
k = Kaavio(25, 18, "Paine edestä ja takaa 2v2", scale=0.85)
for x, y in [(0, 0), (25, 0), (0, 18), (25, 18)]:
    k.cone(x, y, "corner")
k.zone(20, 0, 5, 18)                                  # maalintekoalue
k.cone(20, 0, "line"); k.cone(20, 18, "line")         # viiva 5 m pikkumaalien edessä
k.line(20, 0, 20, 18, dashed=True)
k.goal(0, 6.5, 5, big=True)                           # iso maali
k.goal(25, 2, 2.5); k.goal(25, 13.5, 2.5)             # pikkumaalit lähellä kulmia
k.p(-1.6, 3.6, "A"); k.p(-1.6, 1.8, "A")              # hyökkääjien jonot ison maalin molemmin puolin
k.p(-1.6, 14.4, "A"); k.p(-1.6, 16.2, "A")
k.p(26.6, 8.0, "B"); k.p(26.6, 10.0, "B")             # edestä painostavien jono pikkumaalien takana
k.p(4.0, 19.6, "B"); k.p(6.0, 19.6, "B")              # takaa tulevien jono ison maalin vieressä sivurajalla
k.p(2.6, 5.0, "A", "1H"); k.ball(3.8, 5.6)            # hyökkääjät lähtevät pallon kanssa
k.p(2.6, 13.0, "A", "2H")
k.p(20.0, 9.0, "B", "1P")                             # edestä painostava viivalla
k.p(2.4, 18.0, "B", "2P")                             # takaa tuleva ison maalin vieressä
k.arrow(4.4, 6.0, 11.0, 7.4, "drib")                  # kuljetus kohti pikkumaaleja
k.arrow(3.8, 13.0, 11.0, 12.4, "run")                 # toinen hyökkääjä tukee
k.arrow(19.2, 9.0, 13.6, 8.4, "run")                  # 1P vastaan ja hidastaa
k.arrow(3.6, 17.6, 12.4, 15.2, "run")                 # 2P spurttaa takaa
k.p(12.5, 19.6, "K")                                  # valmentaja sivurajalla
k.text(22.5, -0.8, "maalintekoalue", 10)
k.dim("25 m", "18 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu")],
       png="--png" in sys.argv)
