"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 18 m (iso maali vasemmalla, pikkumaalit oikealla), leveys 15 m; hyökkäys oikealle.
k = Kaavio(18, 15, "Läpimurto pikkumaaleihin 1v1")
for x, y in [(0, 0), (18, 0), (0, 15), (18, 15)]:
    k.cone(x, y, "corner")
k.goal(0, 5, 5, big=True)                             # iso maali
k.goal(18, 1.5, 2); k.goal(18, 11.5, 2)               # pikkumaalit lähellä kulmia
k.zone(15, 0, 3, 15)                                  # maalintekoalue viivan ja pikkumaalien välissä
k.cone(15, 0, "line"); k.cone(15, 15, "line")         # viiva 3 m pikkumaalien edessä
k.line(15, 0, 15, 15, dashed=True)
k.p(1.2, 3.4, "A", "H"); k.ball(2.3, 3.8)             # hyökkääjä pallon kanssa
k.p(-1.4, 3.0, "A"); k.ball(-1.4, 1.8)                # hyökkääjien jono palloineen
k.p(-1.4, 0.2, "A"); k.ball(-1.4, -1.0)
k.p(15.0, 7.5, "B", "P")                              # puolustaja viivalla
k.p(20.0, 6.6, "B"); k.p(20.0, 8.4, "B")              # puolustajien jono pikkumaalien takana
k.arrow(2.8, 4.2, 8.6, 6.4, "drib")                   # kuljetus kovassa vauhdissa
k.arrow(14.4, 7.5, 11.2, 7.3, "run")                  # puolustaja vastaan
k.arrow(9.2, 6.8, 15.6, 11.4, "drib")                 # suunnanmuutos ja kuljetus maalintekoalueelle
k.arrow(16.0, 11.8, 17.8, 12.4, "shot")               # maali pikkumaaliin maalintekoalueelta
k.p(9.0, 16.4, "K"); k.balls(10.4, 16.4, 2)           # valmentaja sivurajalla palloineen
k.text(16.5, -0.8, "maalintekoalue", 10)
k.dim("18 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("shot", "laukaus")],
       png="--png" in sys.argv)
