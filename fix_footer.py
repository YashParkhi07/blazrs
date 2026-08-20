import glob
import re

# This is the exact 4-column footer they want
new_footer_html = """  <footer>
    <div class="wrap">
      <div class="foot-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; margin-bottom: 40px; text-align: left;">
        
        <!-- Column 1: Logo & About -->
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0; letter-spacing: -0.5px;">Blazrs</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 14px; margin: 0; line-height: 1.6;">Blazrs is a trusted Salesforce implementation partner headquartered in India, helping businesses transform sales, service, manufacturing, automotive, and customer operations with Salesforce.</p>
        </div>

        <!-- Column 2: Quick Links -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
          <h4 style="color: #fff; font-size: 16px; margin: 0; margin-bottom: 8px;">Quick Links</h4>
          <a href="index.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Home</a>
          <a href="about.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">About Us</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Services</a>
          <a href="contact.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Contact Us</a>
        </div>

        <!-- Column 3: Our Services -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
          <h4 style="color: #fff; font-size: 16px; margin: 0; margin-bottom: 8px;">Our Services</h4>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Advisory</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Digital Transformation</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Salesforce CRM Implementation Services</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Application Managed Services</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Training</a>
          <a href="salesforce.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: color 0.2s;">Support & Administration</a>
        </div>

        <!-- Column 4: Contact Info -->
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <h4 style="color: #fff; font-size: 16px; margin: 0; margin-bottom: 8px;">Contact Info</h4>
          
          <div style="display: flex; align-items: center; gap: 12px; color: rgba(255,255,255,0.7); font-size: 14px;">
            <span style="font-size: 16px;">✉️</span> <a href="mailto:contact@blazrs.com" style="color: inherit; text-decoration: none;">contact@blazrs.com</a>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 12px; color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.5;">
            <span style="font-size: 16px; margin-top: 2px;">📍</span> INDIA
          </div>
          
          <div style="display: flex; align-items: center; gap: 16px; margin-top: 8px;">
            <a href="https://www.linkedin.com/company/blazrs/" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">in</a>
            <a href="#" target="_blank" style="color: #fff; text-decoration: none; font-weight: 700; font-size: 16px;">X</a>
          </div>
        </div>
      </div>
      <div class="foot-bottom" style="text-align: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; color: rgba(255,255,255,0.5); font-size: 13px; display: block;">
        Copyright © 2026 All Rights Reserved. Designed by Blazrs.
      </div>
    </div>
  </footer>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()

    # 1. Remove the redundant "Let's light the fuse" div I manually added in the footer
    bad_div_pattern = r'<div style="text-align: center; margin-bottom: 60px; padding-bottom: 40px; border-bottom: 1px solid rgba\(255,255,255,0\.1\);">\s*<h2 style="font-size: 48px; font-weight: 800; color: #fff; margin: 0; letter-spacing: -1\.5px;">Let\'s light the fuse\.</h2>\s*</div>'
    content = re.sub(bad_div_pattern, "", content)
    
    # 2. Also physically remove the <section class="cta" id="cta"> block from ALL files
    # because they requested: "remove the 'Let's light the fuse.' section above the footer"
    cta_pattern = r'<section class="cta" id="cta">.*?</section>'
    content = re.sub(cta_pattern, "", content, flags=re.DOTALL)
    
    # 3. Replace the ENTIRE footer block with the clean new 4-column footer
    # This ensures blogs.html and post.html get the full beautiful footer perfectly.
    footer_pattern = r'<footer>.*?</footer>'
    content = re.sub(footer_pattern, new_footer_html, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(content)

print("Done updating all HTML files.")
