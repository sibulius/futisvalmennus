"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 26 m (2 m maalialue + 22 m + 2 m maalialue), leveys 20 m.
k = Kaavio(26, 20, "Alueen puolustaminen 3v3")
k.zone(0, 0, 2, 20); k.zone(24, 0, 2, 20)             # maalialueet
for x, y in [(0, 0), (26, 0), (0, 20), (26, 20)]:
    k.cone(x, y, "corner")
for x in (2, 24):
    k.cone(x, 0, "line"); k.cone(x, 20, "line")       # maalialueiden rajat
# hyökkääjät lähtevät vasemmalta, pallo 1H:lla
k.p(1.0, 14.0, "A", "1H"); k.ball(1.9, 14.8)
k.p(1.0, 8.5, "A", "2H")
k.p(1.0, 3.0, "A", "3H")
# puolustajat: 1P painostaa sisäpuolelta, 2P varmistaa ja sulkee syöttölinjan, 3P tasapaino
k.p(11.0, 12.5, "B", "1P")
k.p(14.0, 9.5, "B", "2P")
k.p(17.0, 5.5, "B", "3P")
k.arrow(10.3, 12.9, 6.2, 14.3, "run")                 # 1P painostaa
k.arrow(13.3, 9.9, 9.2, 11.6, "run")                  # 2P varmistukseen ja syöttölinjalle
k.arrow(16.4, 6.0, 13.2, 7.6, "run")                  # 3P tasapainoon heikolle puolelle
k.arrow(2.6, 15.1, 6.8, 18.0, "drib")                 # 1H ohjautuu lähemmälle sivurajalle
k.arrow(1.8, 8.9, 6.0, 9.6, "run")                    # 2H tarjoutuu
k.arrow(1.8, 3.2, 8.0, 3.0, "run")                    # 3H syvyyteen heikolla puolella
# vaihdossa olevat pelaajat sivulla
for i, c in enumerate("AAABBB"):
    k.p(15.0 + 1.8 * i, 21.8, c)
k.text(19.5, 23.4, "vaihdossa", 10)
k.text(1.0, -0.6, "maalialue", 10); k.text(25.0, -0.6, "maalialue", 10)
k.dim("26 m (2 m + 22 m + 2 m)", "20 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
