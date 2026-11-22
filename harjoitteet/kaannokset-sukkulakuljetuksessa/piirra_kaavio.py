"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Kaista 16 × 8 m; lähtö- ja maaliportti vasemmalla, kääntöviivat 5 m ja 10 m päässä.
k = Kaavio(16, 8, "Käännökset sukkulakuljetuksessa")
k.cone_gate(3, 4, width=4)                              # lähtö- ja maaliportti
for x in (8, 13):                                       # kääntöviivat
    k.line(x, 0.8, x, 7.2, dashed=True)
    k.cone(x, 0.8, "line"); k.cone(x, 7.2, "line")
k.queue(1.2, 4, "A", 3, dx=-1.8)                        # jono, jokaisella oma pallo
k.ball(1.2, 2.8)
k.arrow(3.5, 2.7, 7.6, 2.7, "drib")                     # 1. osuus: 5 m:n viivalle
k.arrow(7.6, 3.6, 3.4, 3.6, "drib")                     # 2. osuus: takaisin lähtöviivalle
k.arrow(3.5, 4.5, 12.6, 4.5, "drib")                    # 3. osuus: 10 m:n viivalle
k.arrow(12.6, 5.4, 2.3, 5.4, "drib")                    # 4. osuus: maaliin portin läpi
k.p(3, 9.4, "K", "V")                                   # valmentaja ajanotossa
k.text(8, -0.5, "5 m", 12, bold=True); k.text(13, -0.5, "10 m", 12, bold=True)
k.dim("n. 16 m", "n. 8 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pelaajat"), ("K", "valmentaja"), ("drib", "kuljetus")],
       png="--png" in sys.argv)
