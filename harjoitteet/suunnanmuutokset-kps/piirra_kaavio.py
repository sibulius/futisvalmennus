"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import math
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Rata: kuusi 6 m:n osuutta, käännökset 45°, 135°, 90°, 135°, 45°.
# Rata on symmetrinen, joten molemmista päistä tulee samat käännökset.
OSUUS, KAANNOKSET = 6, [-45, 135, -90, 135, -45]
pts, a = [(0.0, 0.0)], 45.0
for i in range(6):
    x, y = pts[-1]
    pts.append((x + OSUUS * math.cos(math.radians(a)), y + OSUUS * math.sin(math.radians(a))))
    if i < 5:
        a -= KAANNOKSET[i]
pts = [(x + 4, 12.3 - y) for x, y in pts]                  # kentän koordinaatteihin (y alas)


def suunta(p, q):
    d = math.hypot(q[0] - p[0], q[1] - p[1])
    return (q[0] - p[0]) / d, (q[1] - p[1]) / d


def ulkopuoli(i, m=1.1):
    """Juoksulinja kiertää käännöskartion ulkopuolelta (kolme pistettä kartion ympärillä)."""
    (ax, ay), (bx, by) = suunta(pts[i - 1], pts[i]), suunta(pts[i], pts[i + 1])
    n1 = (-ay, ax) if (-ay * bx + ax * by) < 0 else (ay, -ax)
    n2 = (-by, bx) if (-by * ax + bx * ay) > 0 else (by, -bx)
    ox, oy = ax - bx, ay - by
    n = math.hypot(ox, oy)
    px, py = pts[i]
    return [(px + m * n1[0], py + m * n1[1]), (px + m * ox / n, py + m * oy / n),
            (px + m * n2[0], py + m * n2[1])]


k = Kaavio(25, 16, "Suunnanmuutokset KPS")
for p in pts[1:-1]:                                        # käännöskartiot
    k.cone(*p, "line")
for p, q in [(pts[0], pts[1]), (pts[-1], pts[-2])]:        # porttimaalit radan päihin
    dx, dy = suunta(p, q)
    for s in (-1.1, 1.1):
        k.cone(p[0] - dy * s, p[1] + dx * s, "gate")
for p, q, team in [(pts[0], pts[1], "A"), (pts[-1], pts[-2], "B")]:   # lähtökartio 3 m portin takana, jono sen takana
    dx, dy = suunta(p, q)
    k.cone(p[0] - 3 * dx, p[1] - 3 * dy, "line")
    k.queue(p[0] - 4.3 * dx, p[1] - 4.3 * dy, team, 3, dx=-1.6 * dx, dy=-1.6 * dy)


def juoksu(reitti):
    d = "M" + " L".join(f"{k.X(x):.1f},{k.Y(y):.1f}" for x, y in reitti)
    k.el.append(f'<path d="{d}" fill="none" stroke="#111111" stroke-width="2.5" '
                f'stroke-linejoin="round" marker-end="url(#ah-run)"/>')


def lahto(p, q):
    dx, dy = suunta(p, q)
    return p[0] - 2.5 * dx, p[1] - 2.5 * dy


def kohti(p, q, t):
    return p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])


U = {i: ulkopuoli(i) for i in range(1, 6)}
A0, A1 = U[2][-1], U[3][0]                                  # kohtaamisosuus käännösten 2 ja 3 välissä
juoksu([lahto(pts[0], pts[1]), *U[1], *U[2], kohti(A0, A1, 0.2)])
juoksu([lahto(pts[-1], pts[-2]), *U[5][::-1], *U[4][::-1], *U[3][::-1], kohti(A0, A1, 0.85)])
k.p(*kohti(A0, A1, 0.4), "A")                              # kohtaaminen: KPS kasvokkain
k.p(*kohti(A0, A1, 0.62), "B")
k.p(12.5, 12.8, "K", "V")                                      # valmentaja laskee pisteet
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "punainen ryhmä"), ("B", "sininen ryhmä"), ("K", "valmentaja"),
        ("run", "juoksu")],
       png="--png" in sys.argv)
