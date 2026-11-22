"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 16 m (2 m maalialue + 12 m + 2 m maalialue), leveys 8 m.
k = Kaavio(16, 8, "Hyökkääminen alueelle 1v1")
k.zone(0, 0, 2, 8); k.zone(14, 0, 2, 8)               # maalialueet
for x, y in [(0, 0), (16, 0), (0, 8), (16, 8)]:
    k.cone(x, y, "corner")
for x in (2, 14):
    k.cone(x, 0, "line"); k.cone(x, 8, "line")        # maalialueiden rajat
k.p(1.0, 4.2, "A", "H"); k.ball(1.9, 4.9)             # hyökkääjä lähtee vasemmalta
k.p(8.0, 3.6, "B", "P")
k.arrow(2.6, 5.2, 7.6, 6.4, "drib")                   # kuljetus ohi
k.arrow(8.2, 6.4, 14.4, 6.1, "drib")                  # maalialueelle, pysäytys
k.ball(14.9, 6.1)
k.arrow(8.8, 4.1, 12.6, 5.2, "run")                   # puolustaja perässä
k.arrow(14.8, 5.3, 9.6, 2.4, "drib")                  # maalin jälkeen kohti toista päätyä
# vaihdossa olevat pelaajat sivulla
k.p(5.3, 9.8, "A"); k.p(7.1, 9.8, "A"); k.p(8.9, 9.8, "B"); k.p(10.7, 9.8, "B")
k.text(8.0, 11.4, "vaihdossa", 10)
k.text(1.0, -0.6, "maalialue", 10); k.text(15.0, -0.6, "maalialue", 10)
k.dim("16 m (2 m + 12 m + 2 m)", "8 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
