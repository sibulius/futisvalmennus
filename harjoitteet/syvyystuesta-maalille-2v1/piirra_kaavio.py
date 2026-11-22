"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 14 × 9 m kahtena 7 metrin vyöhykkeenä; maali oikealla, hyökkäys oikealle.
k = Kaavio(14, 9, "Syvyystuesta maalille 2v1")
for x, y in [(0, 0), (14, 0), (0, 9), (14, 9)]:
    k.cone(x, y, "corner")
k.cone(7, 0, "line"); k.cone(7, 9, "line")            # vyöhykeraja
k.line(7, 0, 7, 9, dashed=True)
k.goal(14, 2, 5, big=True)
k.p(13.4, 4.5, "V")                                   # maalivahti
k.queue(9.0, 10.6, "A", 2, dx=1.8); k.ball(12.6, 10.6)  # vaihtopelaajat palloineen maalivyöhykkeen vieressä
k.text(7.2, 10.9, "vaihto", 10, anchor="end")
k.arrow(8.6, 2.2, 4.4, 3.0, "pass")                   # aloitussyöttö maalivyöhykkeestä
k.p(3.6, 3.2, "A", "1H"); k.ball(4.7, 3.6)
k.arrow(5.0, 3.8, 9.4, 4.8, "drib")                   # kuljetus puolustajaa kohti
k.p(10.4, 6.2, "B", "1P")
k.p(9.8, 1.6, "A", "2H")
k.arrow(10.2, 1.8, 12.2, 1.4, "run")                  # pois varjosta syvyyteen
k.arrow(9.6, 4.2, 11.8, 2.0, "pass")
k.arrow(12.4, 1.8, 14, 3.6, "shot")
k.p(3.5, -1.6, "K")                                   # valmentaja sivurajalla
k.queue(9.0, -1.6, "B", 2, dx=1.8)                    # puolustajien vaihtopelaajat
k.text(7.2, -1.3, "vaihto", 10, anchor="end")
k.text(3.5, 4.5 + 3.6, "lähtövyöhyke", 10); k.text(10.5, 8.1, "maalivyöhyke", 10)
k.dim("14 m", "9 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahti"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("pass", "syöttö"), ("shot", "laukaus")],
       png="--png" in sys.argv)
