"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Pituus 14 m (päätyrajalta päätyrajalle), leveys 10 m, 2 m portit. Ei palloja.
k = Kaavio(14, 10, "Ohittaminen ilman palloa 1v1")
for x, y in [(0, 0), (14, 0), (0, 10), (14, 10)]:
    k.cone(x, y, "corner")
for x in (0, 14):
    k.cone_gate(x, 2.5, 2.0); k.cone_gate(x, 7.5, 2.0)  # kaksi porttia kummallakin päätyrajalla
    k.cone(x, 5.0, "line")                           # aloituskartio porttien välissä
k.p(-1.3, 5.0, "A", "H")                              # hyökkääjä aloituskartiolla
k.p(-2.9, 3.7, "A"); k.p(-2.9, 6.3, "A")              # hyökkääjien jono
k.p(15.3, 5.0, "B", "P")                              # puolustaja aloituskartiolla
k.p(16.9, 3.7, "B"); k.p(16.9, 6.3, "B")              # puolustajien jono
k.arrow(-1.0, 4.3, 1.4, 1.6, "run")                   # hyökkääjä oman portin läpi
k.arrow(15.0, 5.8, 12.7, 8.4, "run")                  # puolustaja vastakkaisen puolen portin läpi
k.arrow(2.0, 2.4, 5.5, 4.8, "run")                    # kohti puolustajaa
k.arrow(5.9, 4.8, 7.8, 6.4, "run")                    # harhautus yhteen suuntaan
k.arrow(8.3, 6.1, 14.7, 2.6, "run")                   # suunnanmuutos ja kiihdytys portin läpi
k.arrow(12.2, 7.8, 10.3, 6.8, "run")                  # puolustaja vastaan
k.p(7.0, 11.4, "K")                                   # valmentaja sivurajalla
k.text(0.0, -0.8, "hyökkääjien päätyraja", 10, anchor="start")
k.text(14.0, -0.8, "puolustajien päätyraja", 10, anchor="end")
k.dim("14 m", "10 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "hyökkääjät"), ("B", "puolustajat"), ("K", "valmentaja"), ("run", "juoksu")],
       png="--png" in sys.argv)
