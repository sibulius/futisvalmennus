"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 18 m, leveys 15 m; hyökkääjä hyökkää oikealle pieniin maaleihin.
k = Kaavio(18, 15, "Selkä hyökkäyssuuntaan 1v1")
for x, y in [(0, 0), (18, 0), (0, 15), (18, 15)]:
    k.cone(x, y, "corner")
k.cone(15, 0, "line"); k.cone(15, 15, "line")         # viiva n. 3 m pienten maalien edessä
k.line(15, 0, 15, 15, dashed=True)
k.goal(18, 1.5, 2.5); k.goal(18, 11, 2.5)              # pienet maalit
k.goal(0, 5, 5, big=True)                              # iso maali
# jonot pienten maalien takana: hyökkääjät ja puolustajat
k.queue(20.2, 5.0, "A", n=2, dx=0, dy=1.7)
k.queue(20.2, 8.6, "B", n=2, dx=0, dy=1.7)
# aloitus: puolustaja viivalla, hyökkääjä hänen edessään selkä pieniin maaleihin
k.p(15, 7.5, "B", "P")
k.p(13.2, 7.5, "A", "H")
k.p(-2.0, 12.0, "K"); k.balls(-3.2, 14.0)              # valmentaja ison maalin vieressä
k.arrow(-1.0, 11.4, 12.2, 7.9, "pass")                 # syöttö hyökkääjälle
k.arrow(13.0, 6.6, 15.2, 3.6, "drib")                  # käännös vapaalle puolelle
k.arrow(15.6, 3.2, 17.8, 2.8, "shot")                  # laukaus pieneen maaliin
k.arrow(15.3, 6.6, 15.8, 4.6, "run")                   # puolustaja painostaa takaa
k.text(15, -0.8, "viiva", 10)
k.dim("18 m", "15 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
