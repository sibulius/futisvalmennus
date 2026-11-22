"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(30, 20, "Avaamisen loppupeli 3v3")
for x, y in [(0, 0), (30, 0), (0, 20), (30, 20), (10, 0), (10, 20), (20, 0), (20, 20)]:
    k.cone(x, y, "corner")
k.line(10, 0, 10, 20, dashed=True); k.line(20, 0, 20, 20, dashed=True)
k.text(5, 1.6, "avausvyöhyke", 10); k.text(15, 1.6, "keskivyöhyke", 10); k.text(25, 1.6, "avausvyöhyke", 10)
k.goal(0, 7.5, 5, big=True); k.goal(30, 7.5, 5, big=True)
# punainen avaa maalivahdilta oikealle: MV + 2v1, yksi keskivyöhykkeellä
k.p(1.0, 10, "V", "MV"); k.ball(1.9, 10.7)
k.p(5.5, 3.5, "A", "1H")
k.p(6.0, 16.0, "A", "2H")
k.p(15.0, 9.0, "A")
# sininen: yksi prässääjä avausvyöhykkeellä, kaksi keskellä
k.p(7.0, 9.5, "B", "1P")
k.p(16.0, 6.5, "B"); k.p(14.5, 13.0, "B")
k.p(29.0, 10, "V", "MV")
k.arrow(2.1, 10.9, 5.3, 15.2, "pass")    # MV -> 2H
k.arrow(7.2, 10.4, 6.6, 14.4, "run")     # 1P painostaa
k.arrow(6.9, 15.8, 11.6, 15.0, "drib")   # 2H avaa keskivyöhykkeelle
k.arrow(5.9, 4.3, 9.0, 6.2, "run")       # 1H uuteen syöttökulmaan
k.p(13.5, 21.6, "K", "V"); k.balls(15.1, 21.6, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahdit"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")],
       png="--png" in sys.argv)
