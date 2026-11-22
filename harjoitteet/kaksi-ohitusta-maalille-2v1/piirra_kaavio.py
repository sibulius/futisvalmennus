"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 14 × 9 m kolmena vyöhykkeenä; maali oikealla, hyökkäys oikealle.
k = Kaavio(14, 9, "Kaksi ohitusta maalille 2v1")
for x, y in [(0, 0), (14, 0), (0, 9), (14, 9)]:
    k.cone(x, y, "corner")
for xr in (4.7, 9.3):                                 # vyöhykerajat
    k.cone(xr, 0, "line"); k.cone(xr, 9, "line")
    k.line(xr, 0, xr, 9, dashed=True)
k.goal(14, 2, 5, big=True)
k.p(13.4, 4.5, "V")
k.p(4.7, 3.6, "B", "1P"); k.p(9.3, 4.5, "B", "1P")
k.queue(-2.0, 2.6, "A", 2, dx=-1.8); k.queue(-2.0, 7.0, "A", 2, dx=-1.8)
k.ball(-2.0, 1.4)
k.p(0, 2.6, "A", "1H"); k.ball(1.1, 3.0)
k.p(0, 7.0, "A", "2H")
k.arrow(1.6, 3.4, 3.6, 3.6, "drib")                   # kuljetus ensimmäistä puolustajaa kohti
k.arrow(3.8, 4.2, 6.0, 6.8, "pass")                   # syöttö ensimmäisen ohi
k.arrow(0.8, 7.4, 6.0, 7.6, "run")
k.arrow(6.6, 7.2, 9.0, 7.6, "drib")                   # toinen 2v1: kuljetus ohi
k.arrow(1.0, 2.2, 8.6, 1.4, "run")                    # 1H tukee leveydessä
k.arrow(10.2, 7.4, 14, 5.4, "shot")
k.p(7.0, -1.6, "K")                                   # valmentaja sivurajalla
k.text(2.35, 10.0, "lähtö", 10); k.text(11.65, 10.0, "laukaus", 10)
k.dim("14 m", "9 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahti"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("pass", "syöttö"), ("shot", "laukaus")],
       png="--png" in sys.argv)
