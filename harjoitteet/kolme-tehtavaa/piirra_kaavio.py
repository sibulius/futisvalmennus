"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(25, 20, "Kolme tehtävää")
for x, y in [(0, 0), (25, 0), (0, 20), (25, 20)]:
    k.cone(x, y, "corner")
# pallolliset (punainen)
k.p(6.0, 6.0, "A"); k.ball(6.9, 6.5)
k.p(18.5, 4.5, "A"); k.ball(19.4, 5.0)
k.p(5.0, 15.5, "A"); k.ball(5.9, 16.0)
k.p(15.5, 13.0, "A"); k.ball(16.4, 13.5)
# riistäjät (sininen)
k.p(10.0, 8.5, "B")
k.p(21.0, 9.0, "B")
k.p(9.5, 17.5, "B")
k.p(13.0, 3.0, "B")
# hippaajat liivit kädessä (keltainen)
k.p(14.5, 9.0, "C")
k.p(2.5, 10.5, "C")
k.p(20.5, 16.5, "C")
k.p(3.5, 2.5, "C")
k.arrow(9.4, 7.8, 7.6, 6.6, "run")        # riistäjä prässää pallollista
k.arrow(7.0, 5.6, 10.5, 3.3, "drib")      # pallollinen suojaa ja kuljettaa pois
k.arrow(13.7, 8.9, 10.9, 8.6, "run")      # hippaaja jahtaa riistäjää
k.arrow(20.7, 9.8, 17.0, 12.6, "run")     # riistäjä prässää toista pallollista
k.arrow(20.0, 15.7, 21.0, 10.2, "run")    # hippaaja jahtaa riistäjää takaa
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pallolliset"), ("B", "riistäjät (ei mitään)"), ("C", "liivi kädessä"),
        ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
