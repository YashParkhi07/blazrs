import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Pillars (Remove Salesforce specific, Re-add Stats)
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
            <p class="pillar-description">We refuse to outsource complexity. Our dedicated in-house team brings nearly a decade of battle-tested, hands-on experience across CRM architecture, advanced marketing operations, artificial intelligence integration, and enterprise-grade technology ecosystems. We understand the nuanced landscape of modern digital transformation inside and out, allowing us to anticipate technical roadblocks before they happen and architect resilient systems that scale effortlessly alongside your growing organization.</p>
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

        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-value">8.5+</div>
            <div class="stat-label">Years of experience</div>
          </div>
          <div class="stat-item">
            <div class="stat-value">50+</div>
            <div class="stat-label">Projects shipped</div>
          </div>
          <div class="stat-item">
            <div class="stat-value">30+</div>
            <div class="stat-label">Companies served</div>
          </div>
        </div>
      </div>
    </section>"""

pattern_pillars = r'<section id="pillars" class="pillars-section">.*?</section>'
html = re.sub(pattern_pillars, new_pillars, html, flags=re.DOTALL)


# 2. Elaborate Values Timeline
new_values = """<section id="values" class="values-section">
      <div class="mission-container">
        <div class="section-header">
          <div class="section-label">What we believe in</div>
          <h2>Our values shape every interaction</h2>
          <p>These aren't just words on a wall—they're the fundamental laws of how we operate, make critical decisions, and build lasting relationships with our clients</p>
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Customer Obsession</h3>
              <p class="timeline-description">We don't start with technology; we start with you. We begin every project by immersing ourselves entirely in your business model, your market challenges, and your ultimate goals. Your roadblocks become our roadblocks. Your wins become our wins. We proactively anticipate your needs and build intuitive, frictionless experiences that delight both your internal teams and your end customers, ensuring every solution we deliver is precisely tailored to propel you forward.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Radical Honesty</h3>
              <p class="timeline-description">We will always tell you what we truly think, not simply what you want to hear. If a proposed strategy won't yield the ROI you expect, or if a requested feature is unnecessarily complex, we will explicitly say so—and immediately offer smarter, more efficient alternatives. We believe that true partnership and unshakeable trust are built entirely on transparency, direct communication, and a shared commitment to finding the absolute best path forward, even if it requires difficult conversations.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Relentless Quality</h3>
              <p class="timeline-description">Excellence is not a milestone for us; it is a non-negotiable baseline. From the underlying code architecture we deploy, to the pixel-perfect interfaces we design, down to the clarity of our daily communication, we maintain uncompromising standards at every single touchpoint. We know that small details compound over time, so we rigorously test, audit, and refine our deliverables to ensure they are secure, scalable, and built to withstand the pressures of a rapidly evolving digital ecosystem.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Always Learning</h3>
              <p class="timeline-description">Technology evolves at a blistering pace, and resting on past knowledge is a recipe for obsolescence. We aggressively invest our time and resources into staying ahead of global trends, mastering emerging tools, and deepening our technical expertise across artificial intelligence, cloud infrastructure, and modern enterprise strategy. By continuously sharpening our own skills, we ensure that you are always armed with cutting-edge capabilities and innovative methodologies that keep you miles ahead of your competition.</p>
            </div>
          </div>
        </div>
      </div>
    </section>"""

pattern_values = r'<section id="values" class="values-section">.*?</section>'
html = re.sub(pattern_values, new_values, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

