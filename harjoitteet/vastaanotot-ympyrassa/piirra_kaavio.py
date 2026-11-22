"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import math
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio, WHITE, ZONE  # noqa: E402

# Ympyrä, halkaisija n. 16 m (lähteessä 15–18 m), piirretty 16 × 16 m alueelle.
k = Kaavio(16, 16, "Vastaanotot ympyrässä")
R, C = 8, 8
k.el.append(f'<circle cx="{k.X(C)}" cy="{k.Y(C)}" r="{R * k.S}" fill="{ZONE}" stroke="{WHITE}" stroke-width="2"/>')
for i in range(8):                                     # rajakartiot kehällä
    a = math.radians(22.5 + 45 * i)
    k.cone(C + R * math.cos(a), C + R * math.sin(a), "line")
# kehäpelaajat (syöttäjät) palloineen ympyrän ulkopuolella
for x, y, bx, by in [(1.3, 1.3, 2.5, 0.8), (14.7, 1.3, 13.5, 0.8),
                     (1.3, 14.7, 2.5, 15.2), (14.7, 14.7, 13.5, 15.2)]:
    k.p(x, y, "C"); k.ball(bx, by)
# keskipelaajat
k.p(6.2, 9.4, "A"); k.p(9.6, 10.2, "A")
k.p(5.8, 7.0, "A", "H")
k.arrow(6.6, 6.3, 9.6, 4.6, "run")                     # vinosti kohti vapaata syöttäjää
k.arrow(13.9, 1.9, 10.6, 4.0, "pass")                  # syöttö, palautus samaa linjaa
k.arrow(10.4, 5.4, 11.8, 10.6, "run")                  # hakee seuraavan syöttäjän
k.p(18.2, 13.4, "K"); k.balls(17.4, 15.2)              # valmentaja
k.dim("halkaisija n. 16 m", "n. 16 m")
k.save(str(TAMA / "kaavio.svg"),
       [("C", "kehäpelaajat (syöttäjät)"), ("A", "keskipelaajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("run", "juoksu")],
       png="--png" in sys.argv)
