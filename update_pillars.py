import re

with open('index.html', 'r') as f:
    html = f.read()

# Define the new pillars section without the stats grid and with expanded text
new_pillars = """<section id="pillars" class="pillars-section">
      <div class="mission-container">
        <div class="section-header">
          <div class="section-label">How we operate</div>
          <h2>Three pillars of our approach</h2>
          <p>Every engagement is built on these core principles that guide our decisions and define our impact</p>
        </div>

        <div class="pillars-grid">
          <div class="pillar">
            <div class="pillar-number">01</div>
            <h3 class="pillar-title">Deep Expertise & Strategic Vision</h3>
            <p class="pillar-description">We refuse to outsource complexity. Our dedicated in-house team brings nearly a decade of battle-tested, hands-on experience across the entire Salesforce ecosystem, advanced marketing operations, artificial intelligence integration, and enterprise-grade technology architecture. We understand the nuanced landscape of modern digital transformation inside and out, allowing us to anticipate technical roadblocks before they happen and architect resilient systems that scale effortlessly alongside your growing organization.</p>
          </div>

          <div class="pillar">
            <div class="pillar-number">02</div>
            <h3 class="pillar-title">Relentlessly Outcome-Driven</h3>
            <p class="pillar-description">We believe that beautiful technology is useless if it doesn't move the needle. Metrics matter to us just as much as they matter to you. Every digital strategy we propose is rigorously validated by empirical data, and every technical implementation is continuously measured against tangible business KPIs. We are obsessively focused on delivering measurable, high-impact results—whether that's accelerating sales cycles, reducing operational overhead, or driving unprecedented customer retention.</p>
          </div>

          <div class="pillar">
            <div class="pillar-number">03</div>
            <h3 class="pillar-title">A True Partnership Mindset</h3>
            <p class="pillar-description">We are not just another transactional vendor—we act as an extension of your own team, deeply invested in your long-term success. Transparent communication, brutally honest feedback, and radical accountability define every interaction you will have with us. We take the time to deeply understand the unique cultural and operational fabric of your business, ensuring that we don't just deliver software, but rather a holistic transformation that empowers your people to do their best work.</p>
          </div>
        </div>
      </div>
    </section>"""

# Use regex to find the old pillars section (including the stats grid) and replace it
pattern = r'<section id="pillars" class="pillars-section">.*?</section>'
new_html = re.sub(pattern, new_pillars, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_html)

