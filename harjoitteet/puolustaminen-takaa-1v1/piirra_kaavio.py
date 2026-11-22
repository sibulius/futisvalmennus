"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 15 m (lähtöraja vasemmalla, päätyraja oikealla), leveys 8 m; hyökkäys oikealle.
k = Kaavio(15, 8, "Puolustaminen takaa 1v1", scale=1.3)
for x, y in [(0, 0), (15, 0), (0, 8), (15, 8)]:
    k.cone(x, y, "corner")
k.zone(10, 0, 5, 8)                                   # maalintekoalue
k.cone(10, 0, "line"); k.cone(10, 8, "line")          # maalintekoalueen raja
k.line(10, 0, 10, 8, dashed=True)
k.goal(15, 3, 2)                                      # pikkumaali päätyrajalla
k.cone(3, 1.8, "line"); k.cone(3, 6.2, "line")        # rajakartiot noin 4 m päässä toisistaan
k.p(2.1, 1.8, "B", "P")                              # puolustaja ylemmällä rajakartiolla
k.ball(3.0, 4.0)                                      # pallo pysäytetty rajakartioiden puoliväliin
k.cone(1.2, 4.0, "line")                              # hyökkääjän rajakartio
k.p(0.4, 4.0, "A", "H")                               # hyökkääjä omalla rajakartiollaan
k.p(-1.8, 3.2, "B"); k.p(-1.8, 4.8, "A")              # parijono lähtörajan takana
k.p(-3.5, 3.2, "B"); k.p(-3.5, 4.8, "A")
k.arrow(3.0, 2.3, 3.0, 3.5, "drib")                   # puolustaja kuljettaa ja pysäyttää pallon puolivälissä
k.arrow(2.4, 4.5, 2.4, 6.6, "run")                    # puolustaja kiertää vastakkaisen rajakartion
k.arrow(2.6, 7.0, 9.6, 5.2, "run")                    # aktiivinen puolustaminen takaa
k.arrow(1.6, 4.0, 2.5, 4.0, "run")                    # hyökkääjä lähtee pallolle
k.arrow(3.6, 3.7, 11.2, 3.6, "drib")                  # hyökkääjä kuljettaa kohti päätyä
k.arrow(11.8, 3.7, 14.9, 4.0, "shot")                 # laukaus pikkumaaliin
k.p(7.5, 9.4, "K")                                    # valmentaja sivurajalla
k.text(0.0, -0.8, "lähtöraja", 10, anchor="start")
k.text(15.0, -0.8, "päätyraja", 10, anchor="end")
k.text(12.5, 8.9, "maalintekoalue", 10)
k.dim("15 m", "8 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "juoksu"), ("shot", "laukaus")],
       png="--png" in sys.argv)
