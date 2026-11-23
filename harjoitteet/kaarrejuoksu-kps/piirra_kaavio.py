"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import math
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Juoksu kaaren ulkopuolella. Puolikaari: halkaisija 20 m, säde 10 m → kaaren pituus noin 31 m.
CX, CY, R = 12, 13, 10


def kaari(kulma, r=R):
    a = math.radians(kulma)
    return CX + r * math.cos(a), CY - r * math.sin(a)


k = Kaavio(24, 14, "Kaarrejuoksu KPS")
for kulma in range(15, 166, 15):                           # radan kartiot
    k.cone(*kaari(kulma), "line")
k.cone_gate(CX - R - 1.1, CY + 0.6, width=2.2, vertical=False)   # punaisten porttimaali
k.cone_gate(CX + R + 1.1, CY + 0.6, width=2.2, vertical=False)   # sinisten porttimaali
k.queue(CX - R - 1.1, 15.8, "A", 3, dx=-1.8)                     # jonot porttimaalien takana
k.queue(CX + R + 1.1, 15.8, "B", 3, dx=1.8)


def juoksu(k1, k2, r=R + 1.1):
    (x1, y1), (x2, y2) = kaari(k1, r), kaari(k2, r)
    sweep = 1 if k1 > k2 else 0
    k.el.append(f'<path d="M{k.X(x1):.1f},{k.Y(y1):.1f} A{r*k.S:.1f},{r*k.S:.1f} 0 0 {sweep} '
                f'{k.X(x2):.1f},{k.Y(y2):.1f}" fill="none" stroke="#111111" stroke-width="2.5" '
                f'marker-end="url(#ah-run)"/>')


juoksu(178, 110)                                           # punainen lähtee vasemmasta päästä
juoksu(2, 70)                                              # sininen lähtee oikeasta päästä
k.p(*kaari(96, R + 1.4), "A")                                       # kohtaaminen: KPS kasvokkain
k.p(*kaari(84, R + 1.4), "B")
k.p(CX, 10.0, "K", "V")                                    # valmentaja laskee pisteet
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punainen ryhmä"), ("B", "sininen ryhmä"), ("K", "valmentaja"),
        ("run", "juoksu")],
       png="--png" in sys.argv)
