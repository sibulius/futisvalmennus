"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

k = Kaavio(20, 16, "Suunnanvalinta vastaanotossa 2v2")
for x, y in [(0, 0), (20, 0), (0, 16), (20, 16)]:
    k.cone(x, y, "corner")
# kaksi pikkumaalia kummassakin päädyssä
k.goal(0, 1.5, 2); k.goal(0, 12.5, 2)
k.goal(20, 1.5, 2); k.goal(20, 12.5, 2)
# puolustajat (sininen) päädyissä (jonot)
k.queue(-1.4, 7.1, "B", 2, dx=0, dy=1.8, label="1P")
k.queue(21.4, 7.1, "B", 2, dx=0, dy=1.8, label="2P")
# hyökkääjät (punainen) pitkillä sivuilla (jonot)
k.queue(10, -1.4, "A", 2, dx=2.4, label="1H")
k.queue(10, 17.4, "A", 2, dx=1.8, label="2H")
# kulku
k.arrow(10, 16.4, 10.6, 0.2, "pass")        # 2H syöttää vastakkaiselle sivulle
k.arrow(10.0, 0.6, 6.2, 3.4, "drib")        # 1H:n ensimmäinen kosketus valitsee suunnan
k.ball(10.75, -0.45)                       # pallo 1H:n jaloissa
k.arrow(-0.4, 7.1, 4.6, 5.2, "run")        # 1P tulee painostamaan
k.arrow(20.4, 7.1, 15.2, 6.2, "run")       # 2P tulee peittämään
k.arrow(9.4, 16.3, 5.4, 11.4, "run")       # 2H tulee tueksi hyökkäyssuuntaan
# valmentaja ja pallot
k.p(6.4, 17.4, "K", "V"); k.balls(2.6, 17.4, 3)
k.dim()
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike")], png="--png" in sys.argv)
