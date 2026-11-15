import os
from PIL import Image, ImageDraw, ImageFont

# Dimensions (1280x720 16:9 standard for Upwork portfolio)
width, height = 1280, 720
img = Image.new("RGB", (width, height), color="#0F172A")
draw = ImageDraw.Draw(img)

# Try default or standard fonts
try:
    title_font = ImageFont.truetype("arialbd.ttf", 38)
    subtitle_font = ImageFont.truetype("arial.ttf", 22)
    code_font = ImageFont.truetype("consola.ttf", 18)
    tag_font = ImageFont.truetype("arialbd.ttf", 16)
except Exception:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    code_font = ImageFont.load_default()
    tag_font = ImageFont.load_default()

# Header Accent Line
draw.rectangle([(0, 0), (width, 8)], fill="#38BDF8")

# Title & Subtitle
draw.text((60, 50), "E-Commerce Scraper & Sheets Sync Pipeline", fill="#F8FAFC", font=title_font)
draw.text((60, 105), "Autonomous Multi-Threaded Data Extraction with Resilient Retries & Automated Spreadsheets", fill="#94A3B8", font=subtitle_font)

# Feature Badges
badges = ["Python 3.12", "BeautifulSoup4", "Exponential Backoff", "Google Sheets API", "UTF-8 CSV Pipeline", "100% Test Coverage"]
badge_x = 60
badge_y = 150
for b in badges:
    bbox = draw.textbbox((0, 0), b, font=tag_font)
    bw = bbox[2] - bbox[0] + 24
    bh = 32
    draw.rounded_rectangle([(badge_x, badge_y), (badge_x + bw, badge_y + bh)], radius=6, fill="#1E293B", outline="#334155", width=1)
    draw.text((badge_x + 12, badge_y + 7), b, fill="#38BDF8", font=tag_font)
    badge_x += bw + 12

# Terminal Window Box (Left side: 60 to 760, y: 210 to 650)
term_x0, term_y0, term_x1, term_y1 = 60, 210, 780, 660
draw.rounded_rectangle([(term_x0, term_y0), (term_x1, term_y1)], radius=10, fill="#020617", outline="#334155", width=2)

# Terminal Header
draw.rounded_rectangle([(term_x0, term_y0), (term_x1, term_y0 + 38)], radius=10, fill="#0F172A")
draw.rectangle([(term_x0, term_y0 + 20), (term_x1, term_y0 + 38)], fill="#0F172A") # square bottom
# Window dots
draw.ellipse([(term_x0 + 16, term_y0 + 14), (term_x0 + 26, term_y0 + 24)], fill="#EF4444")
draw.ellipse([(term_x0 + 34, term_y0 + 14), (term_x0 + 44, term_y0 + 24)], fill="#F59E0B")
draw.ellipse([(term_x0 + 52, term_y0 + 14), (term_x0 + 62, term_y0 + 24)], fill="#10B981")
draw.text((term_x0 + 75, term_y0 + 10), "bash - python main.py --pages 3", fill="#64748B", font=code_font)

# Terminal Content
terminal_lines = [
    ("$ python main.py --pages 3", "#F8FAFC"),
    ("[INFO] Initializing E-Commerce Price Monitor Pipeline v1.0", "#38BDF8"),
    ("[INFO] Target: books.toscrape.com | Thread Pool: 4 workers", "#94A3B8"),
    ("[PAGE 1] Fetching 20 items ... HTTP 200 OK (142ms)", "#10B981"),
    ("[PAGE 2] Fetching 20 items ... HTTP 200 OK (168ms)", "#10B981"),
    ("[PAGE 3] Fetching 20 items ... HTTP 200 OK (155ms)", "#10B981"),
    ("[SUCCESS] Total items extracted & normalized: 60 products", "#38BDF8"),
    ("[METRICS] Avg Price: £35.07 | In Stock: 60/60 (100%)", "#F59E0B"),
    ("[EXPORT] Saved clean UTF-8 CSV: 'ecommerce_export_20261116.csv'", "#10B981"),
    ("[SHEETS] Syncing to Google Sheets via API ... Synced 60 rows", "#38BDF8"),
    ("[STATUS] Pipeline completed in 1.48s with 0 errors.", "#10B981"),
]

line_y = term_y0 + 52
for line_text, color in terminal_lines:
    draw.text((term_x0 + 20, line_y), line_text, fill=color, font=code_font)
    line_y += 32

# Right Side Architecture Cards (820 to 1220)
card_x0, card_x1 = 820, 1220

# Card 1: Resilient Extraction
c1_y0, c1_y1 = 210, 345
draw.rounded_rectangle([(card_x0, c1_y0), (card_x1, c1_y1)], radius=10, fill="#1E293B", outline="#334155", width=1)
draw.text((card_x0 + 20, c1_y0 + 16), "🛡️ Anti-Bot & Retries", fill="#F8FAFC", font=subtitle_font)
draw.text((card_x0 + 20, c1_y0 + 55), "• Exponential backoff (1s, 2s, 4s)\n• Realistic browser User-Agent rotation\n• Strict timeout & exception handling", fill="#94A3B8", font=code_font)

# Card 2: Data Normalization
c2_y0, c2_y1 = 365, 500
draw.rounded_rectangle([(card_x0, c2_y0), (card_x1, c2_y1)], radius=10, fill="#1E293B", outline="#334155", width=1)
draw.text((card_x0 + 20, c2_y0 + 16), "⚡ Data Normalization", fill="#F8FAFC", font=subtitle_font)
draw.text((card_x0 + 20, c2_y0 + 55), "• Automated currency & price cleaning\n• Schema validation & error boundaries\n• Statistical summary metrics calculation", fill="#94A3B8", font=code_font)

# Card 3: Enterprise Integration
c3_y0, c3_y1 = 520, 660
draw.rounded_rectangle([(card_x0, c3_y0), (card_x1, c3_y1)], radius=10, fill="#1E293B", outline="#334155", width=1)
draw.text((card_x0 + 20, c3_y0 + 16), "📊 Cloud Spreadsheets", fill="#F8FAFC", font=subtitle_font)
draw.text((card_x0 + 20, c3_y0 + 55), "• Direct Google Sheets API integration\n• Automated UTF-8 CSV backup\n• Live dashboard sync & alerts", fill="#94A3B8", font=code_font)

# Output path
out_dir = r"C:\Users\manir\.gemini\antigravity\scratch\ecommerce-scraper-sheets-sync"
out_path = os.path.join(out_dir, "ecommerce_pipeline_portfolio_cover.png")
img.save(out_path, quality=95)
print(f"Generated portfolio cover image at: {out_path}")
