"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(40, 25, "Avaamisen loppupeli 4v4")
for x, y in [(0, 0), (40, 0), (0, 25), (40, 25), (13, 0), (13, 25), (27, 0), (27, 25)]:
    k.cone(x, y, "corner")
k.line(13, 0, 13, 25, dashed=True); k.line(27, 0, 27, 25, dashed=True)
k.text(6.5, 1.8, "avausvyöhyke", 10); k.text(20, 1.8, "keskivyöhyke", 10); k.text(33.5, 1.8, "avausvyöhyke", 10)
k.goal(0, 10, 5, big=True); k.goal(40, 10, 5, big=True)
# punainen avaa maalivahdilta oikealle: MV + 3v2, yksi keskivyöhykkeellä
k.p(1.0, 12.5, "V", "MV"); k.ball(1.9, 13.2)
k.p(6.0, 4.0, "A", "1H")
k.p(5.5, 21.0, "A", "2H")
k.p(10.5, 12.5, "A", "3H")
k.p(20.0, 15.0, "A")
# sininen: kaksi prässääjää avausvyöhykkeellä, kaksi keskellä
k.p(8.5, 8.0, "B", "1P")
k.p(9.0, 17.5, "B", "2P")
k.p(21.5, 10.0, "B"); k.p(18.5, 18.0, "B")
k.p(39.0, 12.5, "V", "MV")
k.arrow(2.1, 12.4, 9.4, 12.5, "pass")    # MV -> 3H
k.arrow(11.4, 12.5, 15.6, 12.5, "drib")  # 3H avaa keskivyöhykkeelle
k.arrow(21.0, 14.6, 25.0, 13.4, "run")   # keskipelaaja liikkuu maalia kohti
k.arrow(6.2, 20.4, 11.5, 19.8, "run")    # 2H leveyttä ja syvyyttä
k.p(18.5, 26.6, "K", "V"); k.balls(20.1, 26.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahdit"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
