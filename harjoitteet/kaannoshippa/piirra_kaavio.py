"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

W, H = 20, 5                       # kapea alue
GX, GY, GW = W / 2, H / 2, H       # alueen levyinen porttimaali puolivälissä

k = Kaavio(W, H, "Käännöshippa")
for x, y in [(0, 0), (W, 0), (0, H), (W, H)]:             # alue merkitään kulmakartioilla
    k.cone(x, y, "corner")
k.line(GX, 0, GX, H, dashed=True)                         # puoliväli
k.cone_gate(GX, GY, width=GW)                              # porttimaali
k.queue(-0.9, GY, "A", 2, dx=-1.7)                         # jonot alueen päädyissä
k.queue(W + 0.9, GY, "B", 2, dx=1.7)

k.p(GX + 3.0, GY - 0.8, "A")                               # punainen kääntyi sinisten puoliskolla
k.arrow(GX + 1.9, GY - 0.7, 0.6, GY - 0.3, "run")          # palaa portin läpi omaan jonoon
k.p(GX + 6.5, GY + 1.0, "B")                               # sininen lähti, kun punainen läpäisi portin
k.arrow(GX + 5.3, GY + 0.8, GX + 4.2, GY - 0.1, "run")     # yrittää hipata punaisen
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punainen ryhmä"), ("B", "sininen ryhmä"), ("run", "juoksu")],
       png="--png" in sys.argv)
