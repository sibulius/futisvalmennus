"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 18 m (päätyalue 2 m + pelialue 16 m), leveys 10 m; hyökkäys oikealle.
k = Kaavio(18, 10, "Sivuttaislähdöstä maalille 1v1")
k.zone(0, 0, 2, 10)                                   # päätyalue
for x, y in [(0, 0), (18, 0), (0, 10), (18, 10)]:
    k.cone(x, y, "corner")
k.cone(2, 0, "line"); k.cone(2, 10, "line")           # päätyalueen raja
k.goal(18, 2.5, 5, big=True)
k.p(17.0, 4.5, "V", "MV")
# jonot päätyalueen kulmassa: hyökkääjät palloineen, puolustajat rajan vieressä
k.p(-0.6, -1.5, "A"); k.ball(0.3, -1.1)
k.p(1.4, -1.5, "A"); k.ball(2.3, -1.1)
k.p(4.0, -1.5, "B"); k.p(5.8, -1.5, "B")
# aloitusasento: kumpikin sivuttain maaliin nähden rajan eri puolilla
k.p(1.0, 2.0, "A", "H"); k.ball(1.0, 3.1)
k.p(3.3, 2.2, "B", "P")
k.p(-2.2, 4.0, "K")                                   # valmentaja lähtöpäädyssä
k.arrow(1.2, 3.6, 1.6, 5.6, "drib")                   # käännös / leikkaus päätyalueella
k.arrow(2.2, 6.0, 10.6, 6.6, "drib")                  # hyökkäys maalia kohti
k.arrow(3.3, 3.0, 3.3, 5.0, "run")                    # puolustaja seuraa päätyalueen rajan suuntaisesti
k.arrow(11.2, 6.7, 17.8, 6.9, "shot")                 # laukaus
k.text(1.0, 11.2, "päätyalue", 10)
k.dim("18 m (2 m päätyalue + 16 m pelialue)", "10 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("V", "maalivahti"), ("K", "valmentaja"),
        ("drib", "kuljetus"), ("run", "liike"), ("shot", "laukaus")],
       png="--png" in sys.argv)
