# Writes assets/header-dark.svg and assets/header-light.svg for the GitHub profile.
import sys
out = sys.argv[1]
THEMES = {
    "dark":  dict(bg1="#0B1220", bg2="#121B30", ink="#E6EDF3", muted="#9AA7B8", line="#2A3550",
                  card="#141E35", accent="#2DD4BF", accent_soft="#134E4A"),
    "light": dict(bg1="#FFFFFF", bg2="#F3F6FA", ink="#0F172A", muted="#526072", line="#D5DCE6",
                  card="#FFFFFF", accent="#0F766E", accent_soft="#CCFBF1"),
}
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Cantarell, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace"

def svg(t):
    layers = [("screen", "React · Next.js · Flutter", 70),
              ("api",    "Django · Laravel", 150),
              ("database", "PostgreSQL · Redis", 230)]
    rows = []
    for i, (label, tech, y) in enumerate(layers):
        x = 760 + i * 28
        rows.append(f'''
  <rect x="{x}" y="{y - 30}" width="340" height="56" rx="12" fill="{t['card']}" stroke="{t['line']}"/>
  <circle cx="{x + 26}" cy="{y - 2}" r="6" fill="{t['accent']}"/>
  <text x="{x + 44}" y="{y + 3}" font-family="{MONO}" font-size="17" font-weight="600" fill="{t['ink']}">{label}</text>
  <text x="{x + 322}" y="{y + 3}" text-anchor="end" font-family="{SANS}" font-size="15" fill="{t['muted']}">{tech}</text>''')
    # connectors between the layers (left dots)
    conns = "".join(
        f'<line x1="{760 + i*28 + 26}" y1="{y + 4}" x2="{760 + (i+1)*28 + 26}" y2="{y + 74}" '
        f'stroke="{t["accent"]}" stroke-width="2" stroke-dasharray="3 5" stroke-linecap="round"/>'
        for i, (_, _, y) in enumerate(layers[:-1]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="Zal, full-stack developer: business platforms from database to screen">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" rx="20" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="1199" height="299" rx="20" fill="none" stroke="{t['line']}"/>
  <text x="64" y="92" font-family="{MONO}" font-size="18" fill="{t['accent']}">Hello · Bonjour</text>
  <text x="62" y="168" font-family="{SANS}" font-size="76" font-weight="700" fill="{t['ink']}" letter-spacing="-1.5">I’m Zal</text>
  <text x="64" y="212" font-family="{SANS}" font-size="24" font-weight="600" fill="{t['ink']}">Full-stack developer</text>
  <text x="64" y="246" font-family="{SANS}" font-size="19" fill="{t['muted']}">Business platforms, from database to screen.</text>
  <rect x="64" y="262" width="56" height="4" rx="2" fill="{t['accent']}"/>
  {conns}{''.join(rows)}
</svg>
'''

for name, t in THEMES.items():
    with open(f"{out}/header-{name}.svg", "w") as f:
        f.write(svg(t))
print("ok")
