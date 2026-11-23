"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Siksak-rata: 9 kartiota 2 m välein pituussuunnassa ja 5 m sivusuunnassa vuorotellen.
# Pelaajat katsovat kohti vastakkaista päätyä ja liikkuvat sivulaukalla
# vuorotellen vasemmalle ja oikealle.
YA, YY, YM = 7.5, 2.5, 5.0                                 # ala- ja ylärivi, radan keskilinja
KARTIOT = [(11 + 2 * i, YA if i % 2 == 0 else YY) for i in range(9)]
k = Kaavio(38, 10, "Sivulaukka KPS")
for p in KARTIOT:
    k.cone(*p, "line")
for x in (8, 30):                                          # porttimaalit päätyihin
    k.cone_gate(x, YM, width=2.4)
k.cone(5, YM, "line"); k.cone(33, YM, "line")              # lähtökartiot
k.queue(3.6, YM, "A", 3, dx=-1.8)                          # jonot lähtökartion takana
k.queue(34.4, YM, "B", 3, dx=1.8)


def ulko(p, m=0.8):
    return p[0], p[1] + (m if p[1] == YA else -m)


def kohti(p, q, t):
    return p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])


def laukka(reitti):
    d = "M" + " L".join(f"{k.X(x):.1f},{k.Y(y):.1f}" for x, y in reitti)
    k.el.append(f'<path d="{d}" fill="none" stroke="#111111" stroke-width="2.5" '
                f'stroke-linejoin="round" marker-end="url(#ah-run)"/>')


U = [ulko(p) for p in KARTIOT]
laukka([(5.8, YM), (8, YM), *U[:4], kohti(U[3], U[4], 0.25)])
laukka([(32.2, YM), (30, YM), *U[:3:-1], kohti(U[4], U[3], 0.25)])
k.p(*kohti(U[3], U[4], 0.42), "A")                         # kohtaaminen: KPS kasvokkain
k.p(*kohti(U[3], U[4], 0.62), "B")
k.p(22, 9.2, "K", "V")                                     # valmentaja laskee pisteet
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punainen ryhmä"), ("B", "sininen ryhmä"), ("K", "valmentaja"),
        ("run", "sivulaukka")],
       png="--png" in sys.argv)
