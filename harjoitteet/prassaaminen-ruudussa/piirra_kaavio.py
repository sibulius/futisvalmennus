"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Alue 18 × 18 m; keskellä 12 × 12 m:n ruutu, jono jokaisessa kulmassa.


def nro(x, y, n):
    """Järjestysnumero nuolen viereen."""
    cx, cy = k.X(x), k.Y(y)
    k.el.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#111111" stroke="#ffffff" stroke-width="1.5"/>')
    k.el.append(f'<text x="{cx}" y="{cy+4.5}" font-size="13" font-weight="700" text-anchor="middle" fill="#ffffff" font-family="Arial">{n}</text>')


k = Kaavio(18, 18, "Prässääminen ruudussa")
for x, y in [(3, 3), (15, 3), (3, 15), (15, 15)]:
    k.cone(x, y, "corner")
k.text(9, 2.3, "12 m")
k.p(2.2, 15.8, "A")                                # syöttäjä
k.p(1.1, 16.9, "B")                                # seuraava prässääjä
k.ball(3.0, 15.2)
k.queue(15.8, 15.8, "A", 2, dx=1.1, dy=1.1)        # vastaanottajan kulma
k.queue(15.8, 2.2, "A", 2, dx=1.1, dy=-1.1)        # syöttäjän vastakkainen kulma
k.p(2.2, 2.2, "B")                                 # prässääjä vastaanottajan ristikkäisestä kulmasta
k.p(1.1, 1.1, "A")
k.arrow(3.8, 15.2, 14.4, 15.2, "pass")             # syöttö viereiseen kulmaan
k.arrow(1.4, 14.6, 1.4, 4.6, "run")                # syöttäjä siirtyy toiseen jonoon
k.arrow(3.0, 3.0, 12.9, 12.9, "run")               # prässäys: lähestyminen ja jarrutus
k.arrow(3.4, 14.6, 12.9, 5.1, "run")               # seuraava prässäys ristikkäisestä kulmasta
k.arrow(15.8, 14.6, 16.8, 12.2, "drib")            # ensikosketus pois paineesta
k.arrow(16.6, 11.4, 15.6, 3.6, "pass")             # vastaanottaja syöttää heti eteenpäin
nro(9.0, 16.3, 1)     # syöttö
nro(9.0, 7.0, 2)      # prässäys
nro(0.4, 9.6, 2)      # syöttäjä siirtyy (samaan aikaan)
nro(17.6, 13.6, 3)    # ensikosketus pois paineesta
nro(17.2, 7.5, 4)     # seuraava syöttö
nro(5.2, 11.2, 4)     # seuraava prässäys (samaan aikaan kuin syöttö 4)
k.save(str(TAMA / "kaavio.svg"),
       [("A", "pelaajat"), ("B", "prässääjät"), ("pass", "syöttö"), ("run", "juoksu"),
        ("drib", "kuljetus")],
       png="--png" in sys.argv)
