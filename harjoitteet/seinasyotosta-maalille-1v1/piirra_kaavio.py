"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 20 m (lähtöalue 2 m + 18 m maaliin), leveys 10 m; hyökkäys oikealle.
k = Kaavio(20, 10, "Seinäsyötöstä maalille 1v1")
k.zone(0, 0, 2, 10)                                   # lähtöalue
for x, y in [(0, 0), (20, 0), (0, 10), (20, 10)]:
    k.cone(x, y, "corner")
k.cone(2, 0, "line"); k.cone(2, 10, "line")           # lähtöviiva
k.goal(20, 2.5, 5, big=True)
k.p(19.1, 5, "V", "MV")
# hyökkääjät jonossa lähtöalueella, jokaisella pallo
k.p(1, 6.2, "A", "H"); k.ball(1.6, 7.3)
k.queue(1, 4.3, "A", 2, dx=0, dy=-1.9)
# puolustaja muutaman metrin päässä lähtöviivasta
k.p(5.2, 5.6, "B", "P")
k.arrow(1.9, 5.9, 4.4, 5.4, "pass")                   # syöttö puolustajalle
k.arrow(4.6, 6.2, 2.4, 6.8, "pass")                   # seinäsyöttö takaisin
k.arrow(2.4, 7.8, 11.0, 7.4, "drib")                  # kuljetus lähtöviivan yli
k.arrow(5.9, 6.1, 8.6, 6.5, "run")                    # puolustaja kohti kuljetusta
k.arrow(11.6, 7.0, 19.6, 6.9, "shot")                 # laukaus
k.text(1, 11.3, "lähtöalue", 10)
k.dim("20 m (2 m lähtöalue + 18 m)", "10 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustaja"), ("V", "maalivahti"),
        ("pass", "syöttö"), ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
