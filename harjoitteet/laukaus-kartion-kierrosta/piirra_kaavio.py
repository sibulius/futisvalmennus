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
# hyökkääjät jonossa vinosti, jokaisella pallo
k.p(5.6, 4.0, "A", "H"); k.ball(6.4, 4.9)
k.queue(4.0, 2.6, "A", 2, dx=-1.6, dy=-1.3)
# kartioportti: pallo työnnetään kartioiden välistä, pelaaja kiertää alemman kartion
k.cone(11.0, 7.0); k.cone(8.8, 10.0)
k.arrow(6.8, 5.2, 8.6, 6.4, "drib")                    # kuljetus kohti porttia
k.arrow(8.8, 6.8, 11.6, 9.2, "pass")                   # pallo kartioiden välistä
x1, y1, cx, cy, x2, y2 = k.X(8.0), k.Y(7.0), k.X(7.4), k.Y(13.6), k.X(11.2), k.Y(10.4)
k.el.append(f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="#111111" '
            f'stroke-width="2.5" marker-end="url(#ah-run)"/>')     # juoksu kartion ympäri
k.arrow(12.2, 9.8, 21.4, 9.4, "shot")                 # laukaus
k.dim("n. 22 m", "n. 18 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("V", "maalivahti"), ("drib", "kuljetus"),
        ("pass", "pallon työntö"), ("run", "juoksu"), ("shot", "laukaus")],
       png="--png" in sys.argv)
