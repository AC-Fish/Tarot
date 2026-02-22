import os
from tarot_data import CARDS

OUT_DIR = os.path.join('static', 'images')
os.makedirs(OUT_DIR, exist_ok=True)

def color_for_card(name):
    """Return color scheme dict for card."""
    if '权杖' in name:
        return {'bg': '#f5e6d3', 'border': '#d4a574', 'accent': '#c85', 'text': '#5c3d2e'}
    if '圣杯' in name:
        return {'bg': '#e6f0f8', 'border': '#6b9cbc', 'accent': '#3d7fa3', 'text': '#1a3a4f'}
    if '宝剑' in name:
        return {'bg': '#f0f5ff', 'border': '#7090b8', 'accent': '#4560a0', 'text': '#1a2d4a'}
    if '钱币' in name or 'Pentacles' in name:
        return {'bg': '#f0f8e6', 'border': '#7ab87f', 'accent': '#5a8a5f', 'text': '#2d4a2a'}
    # majors: rich gold/purple
    return {'bg': '#f9f3e6', 'border': '#d4a76a', 'accent': '#8b6f47', 'text': '#3d2817'}

def get_suit_symbol(name):
    """Return suit symbol or empty string."""
    if '权杖' in name:
        return '🔱'
    if '圣杯' in name:
        return '🏆'
    if '宝剑' in name:
        return '⚔'
    if '钱币' in name:
        return '◉'
    return ''

def split_card_name(name):
    """Split card name into Chinese and English parts."""
    parts = name.split(' ', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return name, ''

SVG_TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="520" viewBox="0 0 360 520">
  <defs>
    <filter id="f1" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.15"/>
    </filter>
    <pattern id="weave" width="40" height="40" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="40" y2="40" stroke="#000" stroke-width="0.5" opacity="0.05"/>
      <line x1="40" y1="0" x2="0" y2="40" stroke="#000" stroke-width="0.5" opacity="0.05"/>
    </pattern>
  </defs>

  <!-- outer shadow/frame -->
  <rect x="8" y="8" width="344" height="504" rx="18" fill="none" stroke="#000" stroke-width="1" opacity="0.1"/>

  <!-- main card background -->
  <rect x="12" y="12" width="336" height="496" rx="16" fill="{bg}" stroke="{border}" stroke-width="2.5" filter="url(#f1)"/>

  <!-- texture overlay -->
  <rect x="12" y="12" width="336" height="496" rx="16" fill="url(#weave)"/>

  <!-- decorative top border -->
  <rect x="18" y="18" width="324" height="8" rx="4" fill="{accent}" opacity="0.3"/>

  <!-- corner flourishes (top-left) -->
  <g opacity="0.4">
    <circle cx="28" cy="28" r="6" fill="{accent}"/>
    <line x1="28" y1="22" x2="28" y2="34" stroke="{accent}" stroke-width="1"/>
    <line x1="22" y1="28" x2="34" y2="28" stroke="{accent}" stroke-width="1"/>
  </g>

  <!-- corner flourishes (top-right) -->
  <g opacity="0.4">
    <circle cx="332" cy="28" r="6" fill="{accent}"/>
    <line x1="332" y1="22" x2="332" y2="34" stroke="{accent}" stroke-width="1"/>
    <line x1="326" y1="28" x2="338" y2="28" stroke="{accent}" stroke-width="1"/>
  </g>

  <!-- main content -->
  <g text-anchor="middle">
    <!-- suit symbol (small, top) -->
    <text x="180" y="50" font-size="18" fill="{accent}" opacity="0.5">{suit}</text>

    <!-- Chinese title (line 1) -->
    <text x="180" y="145" font-size="40" font-weight="700" font-family="serif" fill="{text}" letter-spacing="1">{name_cn}</text>

    <!-- English title (line 2) -->
    <text x="180" y="195" font-size="28" font-family="serif" fill="{text}" opacity="0.9" font-style="italic">{name_en}</text>

    <!-- suit symbol (small, bottom) -->
    <text x="180" y="470" font-size="18" fill="{accent}" opacity="0.5">{suit}</text>
  </g>

  <!-- decorative bottom border -->
  <rect x="18" y="494" width="324" height="8" rx="4" fill="{accent}" opacity="0.3"/>

</svg>'''

for card in CARDS:
    cid = card['id']
    name = card['name']
    name_cn, name_en = split_card_name(name)
    colors = color_for_card(name)
    suit = get_suit_symbol(name)
    
    svg = SVG_TEMPLATE.format(
        bg=colors['bg'],
        border=colors['border'],
        accent=colors['accent'],
        text=colors['text'],
        name_cn=name_cn,
        name_en=name_en,
        suit=suit
    )
