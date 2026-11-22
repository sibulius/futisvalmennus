"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 22 × 18 m maalin edessä; hyökkäys oikealle, lähtö vasemmalta (ylhäältä).
k = Kaavio(22, 18, "Laukaus kartion kierrosta")
k.goal(22, 8.5, 5, big=True)
k.p(21.1, 11, "V", "MV")
k.p(23.2, 15.6, "V")                                   # vaihtomaalivahti kentän ulkopuolella
# kolme porttia, kunkin takana kaksi pelaajaa palloineen
# portti 1: suoritus piirretty nuolin; pallo työnnetään kartioiden välistä,
# pelaaja kiertää maalin puoleisen kartion
k.p(5.6, 4.0, "A", "H"); k.ball(6.4, 4.9)
k.p(4.0, 2.7, "A")
k.cone(10.34, 7.47); k.cone(9.68, 8.23)
# portti 2: lähempänä maalia, jyrkempi kulma
k.p(10.4, 2.0, "A"); k.p(8.6, 1.5, "A"); k.ball(11.3, 2.6)
k.cone(15.05, 2.92); k.cone(14.75, 3.88)
# portti 3: maalin toisella puolella, kauempana
k.p(4.8, 15.6, "A"); k.p(3.0, 16.0, "A"); k.ball(5.8, 15.0)
k.cone(9.38, 13.92); k.cone(9.62, 14.88)
k.arrow(6.8, 5.2, 8.6, 6.4, "drib")                    # kuljetus kohti porttia
k.arrow(8.8, 6.8, 11.8, 9.4, "pass")                   # pallo kartioiden välistä
x1, y1, cx, cy, x2, y2 = k.X(8.2), k.Y(7.0), k.X(8.2), k.Y(11.4), k.X(11.4), k.Y(10.2)
k.el.append(f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="#111111" '
            f'stroke-width="2.5" marker-end="url(#ah-run)"/>')     # juoksu kartion ympäri
k.arrow(12.4, 9.9, 21.4, 9.4, "shot")                 # laukaus
k.dim("n. 22 m", "n. 18 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("V", "maalivahdit"), ("drib", "kuljetus"),
        ("pass", "pallon työntö"), ("run", "juoksu"), ("shot", "laukaus")],
       png="--png" in sys.argv)
