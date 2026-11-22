"""Piirtää tämän harjoitteen kaavion: python harjoitteet/<tunniste>/piirra_kaavio.py [--png]"""
import sys
from pathlib import Path

TAMA = Path(__file__).resolve().parent
sys.path.insert(0, str(TAMA.parents[1] / "tools"))
from kaavio import Kaavio  # noqa: E402

# Kaksi rinnakkaista kaistaa: kartiot 8 m päässä toisistaan, kaista noin 2 m, väli 2–3 m.
k = Kaavio(8, 7, "Karkupallo 1v1", scale=1.8)
for y in (1.5, 5.5):
    k.cone(0, y, "line"); k.cone(8, y, "line")        # kierrettävät kartiot
    k.line(0, y, 8, y, dashed=True)                   # raja, jonka yli ei oikaista
    k.p(-0.9, y - 0.6, "A"); k.ball(-0.9, y + 0.5)    # karkaaja pallon kanssa
    k.p(8.9, y + 0.6, "B")                            # jahtaaja vastakkaisella kartiolla
    k.arrow(0.4, y - 0.8, 7.4, y - 0.8, "drib")       # karkaaja kuljettaa yläpuolta
    k.arrow(8.4, y + 1.0, 1.2, y + 1.0, "run")        # jahtaaja juoksee alapuolta samaan kiertosuuntaan
k.text(4.0, 1.95, "raja", 10); k.text(4.0, 5.95, "raja", 10)
k.dim("8 m", "2 kaistaa")
k.save(str(TAMA / "kaavio.svg"),
       [("A", "karkaaja"), ("B", "jahtaaja"), ("drib", "kuljetus"), ("run", "juoksu")],
       png="--png" in sys.argv)
