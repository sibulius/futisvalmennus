"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 25 × 20 m; maali oikealla, hyökkäys oikealle. Vasen jono ylhäällä, oikea alhaalla.
k = Kaavio(25, 20, "Kasvavat aallot 1v0–3v3")
for x, y in [(0, 0), (25, 0), (0, 20), (25, 20)]:
    k.cone(x, y, "corner")
k.cone(0, 5, "line"); k.cone(0, 15, "line")          # jonojen lähtöpaikat aloituslinjalla
k.goal(25, 6.5, 7, big=True)
k.p(24.2, 10, "V")
k.p(-1.4, 5, "A", "H"); k.queue(-1.4, 3.1, "A", 2, dx=0, dy=-1.9)     # vasen jono aloittaa (1v0)
k.p(-1.4, 15, "B"); k.queue(-1.4, 16.9, "B", 2, dx=0, dy=1.9)        # oikea jono hyökkää seuraavaksi
k.p(-2.0, 10, "K"); k.balls(-4.6, 11.5, 3)
k.arrow(-1.4, 9.2, 1.0, 5.8, "pass")                 # 1v0: syöttö vasempaan jonoon
k.arrow(1.6, 5.6, 12.5, 7.0, "drib")
k.arrow(13.2, 7.3, 25, 9.0, "shot")
k.arrow(-1.4, 10.8, 1.0, 14.2, "pass")               # 1v1: seuraava pallo oikeaan jonoon
k.arrow(13.4, 8.6, 9.5, 13.0, "run")                 # laukaisija siirtyy puolustamaan
k.text(0, 21.3, "aloituslinja", 10, anchor="start")
k.dim("25 m", "20 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "vasen jono (aloittaa)"), ("B", "oikea jono"), ("V", "maalivahti"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("shot", "laukaus"), ("run", "juoksu")],
       png="--png" in sys.argv)
