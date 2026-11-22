"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Jonot 20 m päässä toisistaan, keskellä kaksi kartiota 6 m:n päässä toisistaan.
k = Kaavio(24, 12, "Seinäsyöttö ja vastaanotto eteenpäin")
k.cone(4, 6, "line"); k.cone(20, 6, "line")             # jonojen lähtökartiot
k.cone(12, 3, "line"); k.cone(12, 9, "line")            # keskikartiot
k.queue(2.2, 6, "A", 2, dx=-2.0)                          # aloittava jono palloineen
k.ball(2.2, 4.7); k.balls(-0.4, 4.4, 2)
k.queue(21.8, 6, "A", 2, dx=2.0)                          # vastaanottava jono
k.p(13.2, 1.6, "A")                                     # liikkuva pelaaja pelattavana
k.p(13.2, 10.4, "A")                                    # sama pelaaja toisella reunalla
k.arrow(20.8, 5.2, 13.9, 2.1, "run")                    # 1. liikkuu pelattavaksi
k.arrow(3.4, 5.6, 12.3, 2.2, "pass")                    # 2. syöttö
k.arrow(12.2, 1.2, 3.2, 4.8, "pass")                    # 3. seinäsyöttö takaisin
k.arrow(13.2, 2.6, 13.2, 9.6, "run")                    # 4. siirtyy toiselle reunalle
k.arrow(3.6, 6.8, 12.0, 10.4, "pass")                   # 5. syöttö peliasentoon
k.arrow(14.0, 10.0, 20.6, 6.9, "pass")                  # 6. syöttö eteenpäin
k.arrow(2.4, 7.2, 12.0, 11.3, "run")                    # 7. syöttäjä siirtyy reunalle
for x, y, t in [(17.8, 3.0, "1"), (8.0, 4.6, "2"), (7.4, 2.4, "3"),
                (14.0, 6.2, "4"), (7.8, 7.4, "5"), (17.6, 9.4, "6"), (6.2, 10.4, "7")]:
    k.text(x, y, t, 12, bold=True)
k.dim("n. 24 m", "n. 12 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pelaajat"),
        ("pass", "syöttö"), ("run", "juoksu")],
       png="--png" in sys.argv)
