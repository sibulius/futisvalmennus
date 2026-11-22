"""Harjoitekaaviot yhtenäisellä tyylillä (tyyli D). Koordinaatit metreinä, origo kentän vasen yläkulma."""
import math, os

PX_M = 18.2          # pikseliä per metri (isot kentät: scale=0.5–0.65)
BG, PITCH, ZONE = "#4f8a3a", "#6db24f", "#82c463"
WHITE, INK = "#ffffff", "#ffffff"
TEAM = {"A": ("#e0302f", "#7a1010"), "B": ("#2fa8e0", "#0d4f70"), "C": ("#f2d21b", "#8a7a0a"),
        "V": ("#16a34a", "#14532d"), "K": ("#9a9a9a", "#3a3a3a")}
CONE = {"corner": ("#e0457b", "#8a1f45", "kulmakartio"), "line": ("#f2d21b", "#8a7a0a", "rajakartio"),
        "gate": ("#f97316", "#7c2d12", "kartiomaali")}
ARROW = {"pass": ("#ffffff", "8,5", 2.5), "shot": ("#ffffff", "8,5", 3.4),
         "run": ("#111111", "", 2.5), "drib": ("#111111", "", 2.2)}
YELLOW_LINE = "#fde047"


def _wave(x1, y1, x2, y2, amp=3.5, period=11):
    L = math.hypot(x2 - x1, y2 - y1)
    if L < 1: return f"M{x1},{y1}"
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    tail, pts, d = min(14, L * 0.3), [], 0.0
    while d < L - tail:
        o = amp * math.sin(2 * math.pi * d / period)
        pts.append((x1 + ux * d + nx * o, y1 + uy * d + ny * o)); d += 2
    pts.append((x2, y2))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


class Kaavio:
    def __init__(self, w, h, title, scale=1.0):
        self.w, self.h, self.title = w, h, title
        self.S = PX_M * scale
        self.r = 14 if scale >= 0.9 else 11
        self.ML, self.MT = 30 + 4 * self.S, 60 + 3.5 * self.S
        self.el, self.cones = [], set()
        self.el.append(f'<rect x="{self.X(0)}" y="{self.Y(0)}" width="{w*self.S}" height="{h*self.S}" fill="{PITCH}" stroke="{WHITE}" stroke-width="2"/>')

    def X(self, x): return self.ML + x * self.S
    def Y(self, y): return self.MT + y * self.S

    # --- kenttä ---
    def zone(self, x, y, w, h, label="", dashed=False, fill=ZONE):
        d = ' stroke-dasharray="6,5"' if dashed else ""
        self.el.append(f'<rect x="{self.X(x)}" y="{self.Y(y)}" width="{w*self.S}" height="{h*self.S}" fill="{fill}" stroke="{WHITE}" stroke-width="2"{d}/>')
        if label: self.text(x + w / 2, y + h / 2, label, 12, bold=True)

    def gap(self, x, y, w, h):
        """Kentän ulkopuolinen väli (esim. kahden ruudun välissä)."""
        self.el.append(f'<rect x="{self.X(x)}" y="{self.Y(y)-1}" width="{w*self.S}" height="{h*self.S+2}" fill="{BG}"/>')

    def line(self, x1, y1, x2, y2, dashed=False, color=WHITE, width=2):
        d = ' stroke-dasharray="6,5"' if dashed else ""
        self.el.append(f'<line x1="{self.X(x1)}" y1="{self.Y(y1)}" x2="{self.X(x2)}" y2="{self.Y(y2)}" stroke="{color}" stroke-width="{width}"{d}/>')

    def point_line(self, x1, y1, x2, y2):
        """Keltainen pisteviiva / päätyviiva."""
        self.line(x1, y1, x2, y2, color=YELLOW_LINE, width=5)

    def goal(self, x, y, length, vertical=True, big=False):
        """Maali kentän reunalla; piirtyy rajan ulkopuolelle. Iso maali 5 m, pikkumaali 2–3 m."""
        dp = (1.8 if big else 1.2) * self.S
        sw = 3 if big else 2
        if vertical:
            gx = self.X(x) - dp if x <= self.w / 2 else self.X(x)
            self.el.append(f'<rect x="{gx}" y="{self.Y(y)}" width="{dp}" height="{length*self.S}" fill="#e6e6e6" fill-opacity="0.9" stroke="{WHITE}" stroke-width="{sw}"/>')
        else:
            gy = self.Y(y) - dp if y <= self.h / 2 else self.Y(y)
            self.el.append(f'<rect x="{self.X(x)}" y="{gy}" width="{length*self.S}" height="{dp}" fill="#e6e6e6" fill-opacity="0.9" stroke="{WHITE}" stroke-width="{sw}"/>')

    def cone(self, x, y, kind="gate"):
        f, st, _ = CONE[kind]; self.cones.add(kind)
        self.el.append(f'<circle cx="{self.X(x)}" cy="{self.Y(y)}" r="7" fill="{f}" stroke="{st}" stroke-width="1.5"/>')

    def cone_gate(self, x, y, width=1.5, vertical=True):
        """Kartiomaali: kaksi kartiota."""
        if vertical: self.cone(x, y - width / 2); self.cone(x, y + width / 2)
        else: self.cone(x - width / 2, y); self.cone(x + width / 2, y)

    # --- pelaajat ja pallot ---
    def _player(self, cx, cy, team, r):
        f, st = TEAM[team]
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="{st}" stroke-width="2"/>'

    def p(self, x, y, team, label=""):
        """team: A punainen (hyökkääjä/joukkue 1), B sininen (puolustaja/joukkue 2), C keltainen (neutraali/syöttäjä/3), V vihreä MV, K harmaa valmentaja."""
        cx, cy = self.X(x), self.Y(y)
        self.el.append(self._player(cx, cy, team, self.r))
        if label:
            tc = "#111" if team == "C" else "#fff"
            self.el.append(f'<text x="{cx}" y="{cy+4}" font-size="12" font-weight="700" text-anchor="middle" fill="{tc}" font-family="Arial">{label}</text>')

    def queue(self, x, y, team, n=2, dx=-1.8, dy=0, label=""):
        """Jono: ensimmäinen kohdassa (x, y), seuraavat dx/dy välein (oletus vasemmalle)."""
        for i in range(n): self.p(x + i * dx, y + i * dy, team, label if i == 0 else "")

    def ball(self, x, y):
        self.el.append(f'<circle cx="{self.X(x)}" cy="{self.Y(y)}" r="6.5" fill="#ffffff" stroke="#333333" stroke-width="1.5"/>')

    def balls(self, x, y, n=3):
        for i in range(n): self.ball(x + i * 1.0, y)

    # --- nuolet ja teksti ---
    def arrow(self, x1, y1, x2, y2, kind="pass"):
        """kind: pass (valk. katko), shot (valk. katko paksu), run (musta), drib (musta aalto)."""
        col, dash, w = ARROW[kind]
        X1, Y1, X2, Y2 = self.X(x1), self.Y(y1), self.X(x2), self.Y(y2)
        if kind == "drib":
            self.el.append(f'<path d="{_wave(X1,Y1,X2,Y2)}" fill="none" stroke="{col}" stroke-width="{w}" marker-end="url(#ah-{kind})"/>')
        else:
            da = f' stroke-dasharray="{dash}"' if dash else ""
            self.el.append(f'<line x1="{X1}" y1="{Y1}" x2="{X2}" y2="{Y2}" stroke="{col}" stroke-width="{w}"{da} marker-end="url(#ah-{kind})"/>')

    def text(self, x, y, t, size=11, color=WHITE, anchor="middle", bold=False):
        """Vain alueiden nimet (maalialue, pisteviiva). Ei valmennusvihjeitä kentälle."""
        b = ' font-weight="700"' if bold else ""
        self.el.append(f'<text x="{self.X(x)}" y="{self.Y(y)}" font-size="{size}" text-anchor="{anchor}" fill="{color}" font-family="Arial"{b}>{t}</text>')

    def dim(self, label_w=None, label_h=None):
        lw = label_w or f"{self.w:g} m"; lh = label_h or f"{self.h:g} m"
        yt, xr = self.Y(0) - 3 * self.S, self.X(self.w) + 4.4 * self.S
        xm, ym = self.X(self.w / 2), self.Y(self.h / 2)
        self.el.append(f'<line x1="{self.X(0)}" y1="{yt}" x2="{self.X(self.w)}" y2="{yt}" stroke="#fff" stroke-width="1.5" marker-start="url(#dim)" marker-end="url(#dim)"/>')
        tw = len(lw) * 7.5 + 16
        self.el.append(f'<rect x="{xm-tw/2}" y="{yt-11}" width="{tw}" height="22" fill="{BG}"/>')
        self.el.append(f'<text x="{xm}" y="{yt+5}" font-size="14" text-anchor="middle" fill="#fff" font-family="Arial">{lw}</text>')
        self.el.append(f'<line x1="{xr}" y1="{self.Y(0)}" x2="{xr}" y2="{self.Y(self.h)}" stroke="#fff" stroke-width="1.5" marker-start="url(#dim)" marker-end="url(#dim)"/>')
        th = len(lh) * 7.5 + 16
        self.el.append(f'<rect x="{xr-11}" y="{ym-th/2}" width="22" height="{th}" fill="{BG}"/>')
        self.el.append(f'<text x="{xr}" y="{ym}" font-size="14" text-anchor="middle" dominant-baseline="middle" fill="#fff" font-family="Arial" transform="rotate(90 {xr} {ym})">{lh}</text>')

    # --- tallennus ---
    def save(self, path, legend, png=False):
        """legend: lista (tunnus, teksti); tunnus = A/B/C/V/K, pass/shot/run/drib tai point_line. Kartiot lisätään automaattisesti."""
        legend = [l for l in legend if not l[0].startswith("cone")]
        for k in CONE:
            if k in self.cones: legend.append(("cone_" + k, CONE[k][2]))
        W = max(self.X(self.w) + 4.4 * self.S + 30, 520)
        def step(t, txt): return 30 + len(txt) * 6.4 + (8 if t in ARROW else 0)
        rows, lx = 1, 30
        for t, txt in legend:
            if lx + step(t, txt) > W - 10: rows += 1; lx = 30
            lx += step(t, txt)
        H = self.Y(self.h) + 2.6 * self.S + 30 + rows * 24
        defs = ("<defs>" + "".join(f'<marker id="ah-{k}" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="10" refY="5" orient="auto"><path d="M0,0 L12,5 L0,10 z" fill="{v[0]}"/></marker>' for k, v in ARROW.items())
                + '<marker id="dim" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#ffffff"/></marker></defs>')
        head = f'<text x="30" y="28" font-size="16" font-weight="700" fill="#fff" font-family="Arial">{self.title}</text>'
        ly, lx, leg = H - rows * 24 + 6, 30, []
        for t, txt in legend:
            if lx + step(t, txt) > W - 10: ly += 24; lx = 30
            if t in TEAM: leg.append(self._player(lx + 8, ly, t, 8))
            elif t.startswith("cone_"):
                f, st, _ = CONE[t[5:]]; leg.append(f'<circle cx="{lx+8}" cy="{ly}" r="7" fill="{f}" stroke="{st}"/>')
            elif t == "point_line":
                leg.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+16}" y2="{ly}" stroke="{YELLOW_LINE}" stroke-width="5"/>')
            elif t in ARROW:
                col, dash, w = ARROW[t]
                if t == "drib":
                    leg.append(f'<path d="{_wave(lx, ly, lx+22, ly, 2.5, 8)}" fill="none" stroke="{col}" stroke-width="{w}"/>')
                else:
                    da = f' stroke-dasharray="{dash}"' if dash else ""
                    leg.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+22}" y2="{ly}" stroke="{col}" stroke-width="{w}"{da}/>')
                lx += 8
            leg.append(f'<text x="{lx+20}" y="{ly+4}" font-size="12" fill="{INK}" font-family="Arial">{txt}</text>')
            lx += 30 + len(txt) * 6.4
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">'
               f'<rect width="100%" height="100%" fill="{BG}"/>{defs}{head}{"".join(self.el)}{"".join(leg)}</svg>')
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(svg)
        if png:
            import cairosvg
            cairosvg.svg2png(url=path, write_to=path[:-4] + ".png", scale=2)
        return path
