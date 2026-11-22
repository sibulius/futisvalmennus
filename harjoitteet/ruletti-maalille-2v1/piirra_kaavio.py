"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Lähtöraja vasemmalla, maali oikealla; 25 × 18 m; hyökkäys oikealle.
k = Kaavio(25, 18, "Ruletti maalille 2v1", scale=0.85)
for x, y in [(0, 0), (25, 0), (0, 18), (25, 18)]:
    k.cone(x, y, "corner")
k.goal(25, 6.5, 5, big=True)
k.p(24.3, 9.0, "V")
for y in (3, 9, 15):                                  # jonojen kohdat lähtörajalla
    k.cone(0, y, "line")
k.queue(-1.4, 3, "A", 2, dx=-1.8); k.queue(-1.4, 9, "A", 2, dx=-1.8); k.queue(-1.4, 15, "A", 2, dx=-1.8)
for y in (3, 9, 15): k.ball(-1.4, y - 1.2)
# Esimerkkikierros: ylempi jono hyökkää pallon kanssa, keskijono puolustaa, alempi tukee.
k.p(2.0, 3.2, "A", "1H"); k.ball(3.1, 3.6)
k.p(2.0, 9.0, "B", "1P")
k.p(2.0, 14.8, "A", "2H")
k.arrow(3.4, 4.0, 11.0, 6.6, "drib")
k.arrow(3.0, 9.0, 10.4, 8.6, "run")                   # puolustaja reagoi
k.arrow(3.2, 14.6, 15.0, 12.6, "run")                 # 2H pois varjosta
k.arrow(11.4, 6.8, 15.0, 12.0, "pass")
k.arrow(15.6, 12.0, 25, 10.2, "shot")
k.p(12.5, 19.4, "K")
k.text(0, -0.9, "lähtöraja", 10)
k.dim("25 m", "18 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustaja"), ("V", "maalivahti"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("pass", "syöttö"), ("shot", "laukaus")],
       png="--png" in sys.argv)
