"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Ruutu 12 × 12 m (säädetään 10–15 m pelaajamäärän mukaan); jono vasemmalla 4 m päässä.
k = Kaavio(12, 12, "10 sekunnin hippa")
for x, y in [(0, 0), (12, 0), (0, 12), (12, 12)]:
    k.cone(x, 0 if y == 0 else 12, "corner")
k.cone(-4, 4.2, "line")                                   # lähtökartio
k.queue(-4, 6.4, "A", 3, dx=0, dy=1.8)                    # jono
k.arrow(-3.5, 4.0, 4.6, 3.4, "run")                       # hippaaja sprinttaa lähtökartiolta ruutuun
k.p(5.4, 3.3, "A")
k.arrow(6.2, 3.0, 8.6, 2.2, "run")                        # jahtaa lähintä
# ruudun pelaajat väistelevät
k.p(9.4, 2.0, "B"); k.arrow(10.0, 2.4, 10.6, 5.2, "run")
k.p(3.0, 8.6, "B")
k.p(8.0, 9.6, "B")
k.p(10.4, 7.4, "B")
k.p(2.2, 1.8, "B")
k.p(6.0, 6.6, "B")
k.arrow(2.4, 9.4, -2.9, 11.9, "run")                     # hipattu ulos jonon perälle
k.p(5, 14.2, "K", "V")                                    # valmentaja ajanotossa
k.dim("10–15 m", "10–15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hippaaja ja jono"), ("B", "ruudun pelaajat"), ("K", "valmentaja"),
        ("run", "juoksu")],
       png="--png" in sys.argv)
