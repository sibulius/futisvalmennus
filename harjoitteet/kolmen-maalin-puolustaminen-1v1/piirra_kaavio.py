"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 18 m (iso maali vasemmalla, pikkumaali ja sivurajojen kartiomaalit oikealla), leveys 15 m.
k = Kaavio(18, 15, "Kolmen maalin puolustaminen 1v1")
for x, y in [(0, 0), (18, 0), (0, 15), (18, 15)]:
    k.cone(x, y, "corner")
k.goal(0, 5, 5, big=True)                             # iso maali
k.goal(18, 6.5, 2)                                    # pikkumaali päädyn keskellä
k.cone_gate(15.0, 0, 4, vertical=False)               # kartiomaali ylärajalla
k.cone_gate(15.0, 15, 4, vertical=False)              # kartiomaali alarajalla
k.p(1.2, 3.4, "A", "H"); k.ball(2.3, 3.8)             # hyökkääjä pallon kanssa
k.p(-1.4, 3.0, "A"); k.ball(-1.4, 1.8)                # hyökkääjien jono palloineen
k.p(-1.4, 0.2, "A"); k.ball(-1.4, -1.0)
k.p(15.0, 7.5, "B", "P")                              # puolustaja pikkumaalin edessä
k.p(20.0, 6.6, "B"); k.p(20.0, 8.4, "B")              # puolustajien jono pikkumaalin takana
k.arrow(2.8, 4.2, 8.4, 6.6, "drib")                   # hyökkäys kohti kolmea maalia
k.arrow(14.4, 7.5, 10.8, 7.4, "run")                  # puolustaja vastaan
k.arrow(9.0, 7.4, 15.0, 14.6, "drib")                 # auki jäävän kartiomaalin läpi
k.text(15.0, -0.8, "kartiomaali", 10)
k.text(15.0, 16.4, "kartiomaali", 10)
k.p(7.5, 16.4, "K"); k.balls(8.9, 16.4, 2)            # valmentaja sivurajalla palloineen
k.dim("18 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu")],
       png="--png" in sys.argv)
