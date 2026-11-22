"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 24 × 12 m; keskellä 5 × 5 m:n ruutu, jonot ruudun molemmin puolin n. 7 m päässä.
k = Kaavio(24, 12, "Suunnattu vastaanotto ruudussa")
for x, y in [(9.5, 3.5), (14.5, 3.5), (9.5, 8.5), (14.5, 8.5)]:
    k.cone(x, y, "line")                                # ruutu
k.cone(5.8, 6, "line"); k.cone(18.2, 6, "line")         # lähtökartiot
k.queue(4.5, 6, "A", 3, dx=-1.6)                          # vasen jono
k.queue(19.5, 6, "A", 3, dx=1.6)                          # oikea jono, palloja
k.ball(19.5, 7.2); k.ball(21.1, 7.2); k.ball(22.7, 7.2)
k.p(11.2, 6, "A", "H")                                  # vastaanottaja ruudussa
k.arrow(5.4, 6.9, 10.4, 6.9, "run")                     # vastaanottaja tulee vasemmalta jonosta
k.arrow(17.6, 6, 12.2, 6, "pass")                       # syöttö oikealta
k.arrow(19.3, 4.8, 13.4, 4.6, "run")                    # syöttäjä seuraa syöttöä ruutuun
k.arrow(12, 6.9, 13.6, 11.2, "drib")                      # vino ensikosketus eteenpäin ruudun sivusta ulos
k.dim("n. 24 m", "n. 12 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pelaajat"), ("pass", "syöttö"), ("run", "juoksu"), ("drib", "kuljetus")],
       png="--png" in sys.argv)
