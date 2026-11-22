"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 16 m (2 m maalialue + 12 m + 2 m maalialue), leveys 8 m.
k = Kaavio(16, 8, "Alueen puolustaminen 1v1")
k.zone(0, 0, 2, 8); k.zone(14, 0, 2, 8)               # maalialueet
for x, y in [(0, 0), (16, 0), (0, 8), (16, 8)]:
    k.cone(x, y, "corner")
for x in (2, 14):
    k.cone(x, 0, "line"); k.cone(x, 8, "line")        # maalialueiden rajat
k.p(1.0, 4.0, "A", "H"); k.ball(1.9, 4.7)             # hyökkääjä lähtee vasemmalta
k.p(8.5, 3.2, "B", "P")
k.arrow(7.9, 3.5, 6.0, 4.5, "run")                    # puolustaja painostaa sisäpuolelta
k.arrow(2.6, 5.0, 6.2, 6.6, "drib")                   # hyökkääjä ohjautuu sivurajalle
k.arrow(6.6, 6.9, 7.8, 8.5, "drib")                   # pallo yli lähemmän sivurajan
k.ball(8.1, 9.0)
k.arrow(6.3, 5.2, 7.4, 6.3, "run")                    # puolustaja seuraa ja sulkee
# vaihdossa olevat pelaajat sivulla
k.p(10.0, 9.8, "A"); k.p(11.8, 9.8, "A"); k.p(13.6, 9.8, "B"); k.p(15.4, 9.8, "B")
k.text(12.7, 11.4, "vaihdossa", 10)
k.text(1.0, -0.6, "maalialue", 10); k.text(15.0, -0.6, "maalialue", 10)
k.dim("16 m (2 m + 12 m + 2 m)", "8 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
