"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 22 m (2 m maalialue + 18 m + 2 m maalialue), leveys 14 m.
k = Kaavio(22, 14, "Alueen puolustaminen 2v2")
k.zone(0, 0, 2, 14); k.zone(20, 0, 2, 14)             # maalialueet
for x, y in [(0, 0), (22, 0), (0, 14), (22, 14)]:
    k.cone(x, y, "corner")
for x in (2, 20):
    k.cone(x, 0, "line"); k.cone(x, 14, "line")       # maalialueiden rajat
# hyökkääjät lähtevät vasemmalta, pallo 1H:lla
k.p(1.0, 8.5, "A", "1H"); k.ball(1.9, 9.3)
k.p(1.0, 3.0, "A", "2H")
# puolustajat: 1P painostaa sisäpuolelta, 2P varmistaa ja sulkee syöttölinjan
k.p(9.5, 7.5, "B", "1P")
k.p(13.0, 5.0, "B", "2P")
k.arrow(8.8, 7.9, 5.4, 8.8, "run")                    # 1P painostaa
k.arrow(12.3, 5.4, 8.6, 6.6, "run")                   # 2P varmistukseen ja syöttölinjalle
k.arrow(2.6, 9.6, 6.6, 12.0, "drib")                  # 1H ohjautuu lähemmälle sivurajalle
k.arrow(1.8, 3.4, 7.0, 3.2, "run")                    # 2H tarjoutuu
# vaihdossa olevat pelaajat sivulla
k.p(14.4, 15.8, "A"); k.p(16.2, 15.8, "A"); k.p(18.0, 15.8, "B"); k.p(19.8, 15.8, "B")
k.text(17.1, 17.4, "vaihdossa", 10)
k.text(1.0, -0.6, "maalialue", 10); k.text(21.0, -0.6, "maalialue", 10)
k.dim("22 m (2 m + 18 m + 2 m)", "14 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
