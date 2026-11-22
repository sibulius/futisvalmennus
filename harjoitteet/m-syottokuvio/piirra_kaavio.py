"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 28 × 20 m; lähtöpäädyssä paluupelaajat molemmin puolin: lähtökartio – keskikartio n. 14 m, keskikartio – sakarat n. 10 m.
k = Kaavio(28, 20, "M-syöttökuvio")
k.cone(5.2, 11.3, "line")                                # 1: lähtökartio
k.cone(17, 11.4, "line")                                 # 2: keskikartio
k.cone(25, 4.9, "line"); k.cone(25, 17.9, "line")        # 3 ja 4: sakarat
k.queue(4.4, 10, "A", 3, dx=-1.6)                        # jono lähtökartiolla
k.ball(5.4, 9.1); k.ball(3.0, 11.3)
k.p(17, 10, "A"); k.p(25, 3.5, "A"); k.p(25, 16.5, "A")
k.arrow(6, 10, 15.5, 10, "pass")                       # 1 → 2
k.arrow(18.2, 9.1, 23.8, 4.5, "pass")                    # 2 → 3
k.arrow(5.6, 8.3, 15.8, 8.6, "run")                      # syöttäjä seuraa syöttöään
k.arrow(16.6, 8.4, 22.8, 3.6, "run")                     # 2 seuraa syöttöään sakaraan
k.cone(5.2, 5.8, "line"); k.cone(5.2, 16.8, "line")      # paluukartiot molemmin puolin
k.p(4.4, 4.5, "A"); k.p(4.4, 15.5, "A")                  # paluupelaajat
k.arrow(23.7, 3.3, 5.9, 4.4, "pass")                     # 3 → paluupelaaja
k.arrow(24.2, 2.2, 6.0, 2.9, "run")                      # 3 seuraa syöttöään paluupaikalle
k.arrow(3.3, 5.4, 1.4, 8.4, "drib")                      # paluupelaaja jonon perään
k.dim("n. 28 m", "n. 20 m")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pelaajat"), ("pass", "syöttö"), ("run", "juoksu"), ("drib", "kuljetus")],
       png="--png" in sys.argv)
