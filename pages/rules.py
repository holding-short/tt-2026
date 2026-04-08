import json
import streamlit as st
import streamlit.components.v1 as components

# Load config
with open("config.json") as f:
    config = json.load(f)

# Build HTML dynamically
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #ffffff;
    font-family: 'Space Grotesk', sans-serif;
    color: #333;
    padding: 0 4px 16px 4px;
  }}
  .hero {{
    background: #ffffff;
    border-radius: 12px;
    padding: 1.8rem 2.2rem;
    margin-bottom: 1.4rem;
    border: 1px solid #e5e7eb;
  }}
  .hero h1 {{ font-family: 'Space Grotesk', sans-serif; font-size: 2rem; font-weight: 700; color: #111827; }}
  .hero .sub {{ color: #4b5563; font-size: 0.9rem; font-weight: 500;
               letter-spacing: 2px; text-transform: uppercase; margin-top: 0.3rem; }}
  .card {{
    background: #ffffff;
    border-radius: 10px;
    padding: 1.3rem 1.7rem;
    border: 1px solid #e5e7eb;
    box-shadow: none;
  }}
  .card h2 {{ font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; font-weight: 700;
             color: #1a1a2e; margin-bottom: 0.6rem; }}
  .card ul {{ padding-left: 1.2rem; line-height: 1.8; font-size: 0.95rem; color: #444; }}
  .card p  {{ line-height: 1.8; font-size: 0.95rem; color: #444; }}
  .card strong {{ color: #1a1a2e; }}
  .elim {{ color: #e74c3c; font-weight: 700; }}
  .gold-text {{ color: #111827; font-weight: 700; }}
  .rules-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin-bottom: 1.1rem;
  }}
  .rules-grid .card {{
    height: 100%;
  }}
  @media (max-width: 900px) {{
    .rules-grid {{
      grid-template-columns: 1fr;
    }}
  }}
  .footer {{ text-align: center; color: #999; font-style: italic; padding: 0.5rem 0; font-size: 0.9rem; }}
</style>
</head>
<body>

<div class="hero">
  <h1>{emoji} {title}</h1>
  <div class="sub">{subtitle}</div>
</div>

<div class="rules-grid">
{rules_html}
</div>

<div class="footer">{footer}</div>

</body>
</html>
"""

# Build rules cards
rules_html = ""
for rule in config["rules"]:
    rules_html += f"<div class=\"card\">\n  <h2>{rule['emoji']} {rule['title']}</h2>\n"
    if "content" in rule:
        rules_html += f"  <p>{rule['content']}</p>\n"
    if "items" in rule:
        rules_html += "  <ul>\n"
        for item in rule["items"]:
            rules_html += f"    <li>{item}</li>\n"
        rules_html += "  </ul>\n"
    rules_html += "</div>\n"

# Format and render
html_final = html_content.format(
    emoji=config["hero"]["emoji"],
    title=config["hero"]["title"],
    subtitle=config["hero"]["subtitle"],
    rules_html=rules_html,
    footer=config["footer"]
)

components.html(html_final, height=1150, scrolling=False)
