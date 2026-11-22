"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 18 m (iso maali vasemmalla, pikkumaalit oikealla), leveys 15 m; hyökkäys oikealle.
k = Kaavio(18, 15, "Läpimurto pikkumaaleihin 2v1")
for x, y in [(0, 0), (18, 0), (0, 15), (18, 15)]:
    k.cone(x, y, "corner")
k.goal(0, 5, 5, big=True)
k.goal(18, 1.5, 2); k.goal(18, 11.5, 2)
k.zone(15, 0, 3, 15)
k.cone(15, 0, "line"); k.cone(15, 15, "line")
k.line(15, 0, 15, 15, dashed=True)
k.p(1.2, 2.6, "A", "1H"); k.ball(2.3, 3.0)            # pallollinen ylemmästä jonosta
k.p(1.2, 12.4, "A", "2H")                             # pallotonta tukea alemmasta jonosta
k.queue(-1.4, 2.6, "A", 2, dx=0, dy=-1.8); k.ball(-2.5, 2.6)
k.queue(-1.4, 12.4, "A", 2, dx=0, dy=1.8)
k.p(15.0, 7.5, "B", "1P")
k.p(20.0, 6.6, "B"); k.p(20.0, 8.4, "B")
k.arrow(2.8, 3.4, 8.8, 6.0, "drib")                   # kuljetus puolustajaa kohti
k.arrow(14.4, 7.5, 11.0, 7.0, "run")                  # puolustaja spurttaa vastaan
k.arrow(2.0, 12.6, 9.6, 11.6, "run")                  # 2H leveänä
k.arrow(9.2, 6.4, 11.0, 11.0, "pass")                 # syöttö, kun puolustaja sitoutuu
k.arrow(11.6, 11.4, 15.6, 12.4, "drib")
k.arrow(16.0, 12.4, 17.8, 12.6, "shot")
k.p(9.0, 16.4, "K"); k.balls(10.4, 16.4, 2)
k.text(16.5, -0.8, "maalintekoalue", 10)
k.dim("18 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("pass", "syöttö"), ("shot", "laukaus")],
       png="--png" in sys.argv)
