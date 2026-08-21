import re
import glob

html_files = glob.glob('public/*.html')

old_bg = 'background-color: #00A1E0'
new_bg = 'background-color: #000000'

old_desc = 'Blazrs is a trusted Salesforce implementation partner headquartered in India, helping businesses transform sales, service, manufacturing, automotive, and customer operations with Salesforce.'
new_desc = 'Blazrs is a modern technology and strategy consulting firm headquartered in India. We help ambitious businesses simplify complexity, optimize operations, and unlock sustainable growth through comprehensive digital transformation, automation, AI, and data solutions.'

old_social = """          <div style="display: flex; align-items: center; gap: 16px; margin-top: 8px;">
            <a href="https://www.linkedin.com/company/blazrs/" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">in</a>
            <a href="#" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">X</a>
          </div>"""

new_social = """          <div style="display: flex; align-items: center; gap: 16px; margin-top: 8px;">
            <a href="https://www.linkedin.com/company/blazrs/" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">in</a>
            <a href="#" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">X</a>
            <a href="#" target="_blank" style="color: #fff; text-decoration: none; display: flex; align-items: center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
            </a>
          </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_bg, new_bg)
    content = content.replace(old_desc, new_desc)
    content = content.replace(old_social, new_social)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Update styles.css
with open('public/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(old_bg, new_bg)

with open('public/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

