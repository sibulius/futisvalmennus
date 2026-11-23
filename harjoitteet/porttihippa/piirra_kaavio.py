"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
import kaavio  # noqa: E402
from kaavio import Kaavio  # noqa: E402

kaavio.CONE["line"] = (*kaavio.CONE["line"][:2], "lähtökartio")

W, H, GY, GW = 24, 10, 5.0, 2.5   # alue, porttien linja ja leveys
PA, PB = 6, 18                    # porttimaalien keskikohdat 12 m päässä toisistaan
LA = PA - GW / 2 - 3              # lähtökartiot 3 m portin ulkopuolella
LB = PB + GW / 2 + 3
LYA, LYB = GY - 1, GY + 1         # 1 m porttien linjan sivussa: punaiset yläpuolella, siniset alapuolella

k = Kaavio(W, H, "Porttihippa")
k.cone_gate(PA, GY, width=GW, vertical=False)   # punaisten portti
k.cone_gate(PB, GY, width=GW, vertical=False)   # sinisten portti
k.cone(LA, LYA, "line")                          # lähtökartiot
k.cone(LB, LYB, "line")
k.queue(LA - 0.9, LYA, "A", 3, dx=-1.7)          # jonot lähtökartioiden takana
k.queue(LB + 0.9, LYB, "B", 3, dx=1.7)

k.arrow(LA + 0.5, LYA - 0.2, PB - 0.5, GY - 2.4, "run")    # punainen juoksee porttien yläpuolella
k.arrow(PB, GY - 2.2, PB, GY + 2.0, "run")                 # portin läpi
k.arrow(PB - 0.6, GY + 2.4, 12.8, GY + 2.4, "run")         # kääntyy ja palaa alapuolella
k.p(11.4, GY + 2.4, "A")                                    # karkuun juoksija
k.arrow(10.0, GY + 2.3, PA + 0.4, GY + 0.9, "run")         # kohti omaa porttia
k.arrow(LB - 0.4, LYB + 0.3, 15.8, GY + 3.5, "run")        # sininen lähtee portin läpäisyn jälkeen
k.p(14.4, GY + 3.5, "B")                                    # hippaaja
k.arrow(13.2, GY + 3.3, 12.4, GY + 3.0, "run")
k.p(W / 2, 1.6, "K")                                        # valmentaja laskee pisteet
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punainen ryhmä"), ("B", "sininen ryhmä"), ("K", "valmentaja"),
        ("run", "juoksu")],
       png="--png" in sys.argv)
