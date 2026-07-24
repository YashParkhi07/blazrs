import re

html_file = 'salesforce.html'
with open(html_file, 'r') as f:
    content = f.read()

original_section = """<section class="salesforce">
    <div class="wrap">
      <div class="sf-grid">
        <div>
          <div class="sf-badge"><span></span> Full Clouds Coverage</div>
          <h2>One partner, across<br>the whole platform.</h2>
          <p class="sf-copy">Rather than handing off between vendors per cloud, our team carries context from
            discovery through go-live and beyond — across every corner of the Salesforce ecosystem you rely on.</p>
        </div>
        <div class="sf-list">
          <div class="sf-item">
            <h4>Sales Cloud</h4>
            <p>Supercharge your sales teams with advanced pipeline management, AI-driven forecasting, and automated territory design. We customize CPQ (Configure, Price, Quote) workflows tailored exactly to your unique sales motion, ensuring faster deal closures and maximized revenue growth.</p>
          </div>
          <div class="sf-item">
            <h4>Service Cloud</h4>
            <p>Deliver exceptional customer support with intelligent case routing, seamless omnichannel experiences, and robust knowledge management systems. We help you implement self-service portals and automated workflows that significantly shorten resolution times and boost customer satisfaction.</p>
          </div>
          <div class="sf-item">
            <h4>Marketing Cloud</h4>
            <p>Craft highly personalized, data-driven customer journeys using Journey Builder and dynamic AMPscript. We design sophisticated segmentation strategies and cross-channel campaigns that engage your audience at the right time, driving higher conversions and brand loyalty.</p>
          </div>
          <div class="sf-item">
            <h4>Experience Cloud</h4>
            <p>Build immersive, branded digital portals that connect your customers, partners, and employees directly to your core Salesforce data. We create secure, collaborative communities that enhance engagement, streamline onboarding, and foster long-term relationships.</p>
          </div>
          <div class="sf-item">
            <h4>Data Cloud</h4>
            <p>Break down data silos and build unified, 360-degree customer profiles. We help you harmonize fragmented data from across your organization into a single, actionable source of truth, enabling real-time personalization and deeper analytical insights.</p>
          </div>
          <div class="sf-item">
            <h4>Agentforce &amp; AI</h4>
            <p>Step into the future with autonomous agents and Einstein-powered generative AI features. We layer intelligent automation on top of a clean, well-governed data foundation to automate repetitive tasks, predict trends, and deliver proactive, intelligent experiences.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

# Replace the salesforce section
content = re.sub(r'<section class="salesforce">.*?</section>', original_section, content, flags=re.DOTALL)

# Remove the dialog and script from the end
content = re.sub(r'<dialog id="cloud-dialog" class="cloud-dialog">.*?</script>', '', content, flags=re.DOTALL)

# Remove extra blank lines that might have been left at the bottom
content = content.replace('\n\n\n\n</body>', '\n\n</body>')

with open(html_file, 'w') as f:
    f.write(content)

css_file = 'styles.css'
with open(css_file, 'r') as f:
    css_content = f.read()

# Revert sf-item 
sf_item_orig = """    .sf-item {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 18px 20px;
    }"""
css_content = re.sub(r'    \.sf-item \{\n      background: var\(--panel\);\n      border: 1px solid var\(--line\);\n      border-radius: 10px;\n      padding: 18px 20px;\n      cursor: pointer;\n      transition: border-color 0\.2s ease, transform 0\.2s ease;\n    \}\n\n    \.sf-item:hover \{\n      border-color: var\(--cyan\);\n      transform: translateY\(-2px\);\n    \}', sf_item_orig, css_content)

# Remove modal css
css_content = re.sub(r'/\* DIALOG MODAL \*/.*', '', css_content, flags=re.DOTALL)

with open(css_file, 'w') as f:
    f.write(css_content)

