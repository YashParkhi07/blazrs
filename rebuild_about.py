import re

# 1. Get Blazrs header and footer from index.html
with open('index.html', 'r') as f:
    index_html = f.read()

# Extract from <!DOCTYPE html> to </header>
header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', index_html, re.DOTALL)
blazrs_header = header_match.group(1)

# Modify title in header
blazrs_header = re.sub(r'<title>.*?</title>', '<title>Our Mission | Blazrs</title>', blazrs_header)

# Extract footer from <footer> to </html>
footer_match = re.search(r'(<footer>.*</html>)', index_html, re.DOTALL)
blazrs_footer = footer_match.group(1)


# 2. The User's Code
user_code = """
  <style>
    :root {
      --primary: var(--cyan, #00d9ff);
      --accent: #4ade80;
      --bg-dark: var(--bg, #0b1021);
      --text-primary: #ffffff;
      --text-secondary: rgba(255, 255, 255, 0.7);
      --text-muted: rgba(255, 255, 255, 0.5);
    }

    /* Wave Animation Background */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideLeft {
      from { opacity: 0; transform: translateX(-50px); }
      to { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideRight {
      from { opacity: 0; transform: translateX(50px); }
      to { opacity: 1; transform: translateX(0); }
    }
    @keyframes scaleIn {
      from { opacity: 0; transform: scale(0.8); }
      to { opacity: 1; transform: scale(1); }
    }
    @keyframes morphShape {
      0%, 100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
      50% { border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; }
    }
    @keyframes float {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-20px); }
    }
    @keyframes shimmer {
      0% { background-position: -1000px 0; }
      100% { background-position: 1000px 0; }
    }

    body {
      background: var(--bg-dark);
      color: var(--text-primary);
    }

    /* We map container to wrap to match Blazrs */
    .mission-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* Hero Section */
    .mission-hero {
      min-height: 80vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 8rem 0 4rem;
    }
    .mission-hero::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 20% 50%, rgba(0, 217, 255, 0.1) 0%, transparent 50%),
                  radial-gradient(circle at 80% 80%, rgba(74, 222, 128, 0.05) 0%, transparent 50%);
      animation: float 6s ease-in-out infinite;
      pointer-events: none;
    }
    .hero-content {
      position: relative;
      z-index: 2;
      text-align: center;
      max-width: 800px;
    }
    .mission-hero h1 {
      font-size: clamp(2.5rem, 8vw, 4.5rem);
      font-weight: 700;
      line-height: 1.1;
      margin-bottom: 1.5rem;
      animation: fadeUp 0.8s ease-out 0.2s both;
      color: #fff;
    }
    .mission-hero h1 .word {
      display: inline-block;
    }
    .mission-hero h1 .word:nth-child(2) { color: var(--accent); }
    .mission-hero h1 .word:nth-child(4) { color: var(--primary); }

    .hero-description {
      font-size: 1.2rem;
      color: var(--text-secondary);
      margin-bottom: 2.5rem;
      line-height: 1.8;
      animation: fadeUp 0.8s ease-out 0.6s both;
    }
    .hero-cta {
      display: inline-flex;
      gap: 1rem;
      animation: fadeUp 0.8s ease-out 0.8s both;
    }
    
    .m-btn {
      padding: 1rem 2.5rem;
      border: 2px solid var(--accent);
      background: transparent;
      color: var(--text-primary);
      border-radius: 30px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s;
      text-decoration: none;
      display: inline-block;
    }
    .m-btn-primary {
      background: linear-gradient(135deg, var(--accent), var(--primary));
      border-color: transparent;
      color: #000;
    }
    .m-btn-primary:hover {
      transform: translateY(-4px);
      box-shadow: 0 15px 40px rgba(74, 222, 128, 0.3);
    }
    .m-btn-secondary {
      border-color: var(--primary);
      color: var(--primary);
    }
    .m-btn-secondary:hover {
      background: rgba(0, 217, 255, 0.1);
      transform: translateY(-4px);
    }

    /* Mission Statement */
    .mission-section { padding: 6rem 0; position: relative; }
    .mission-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
    .mission-text h2 { font-size: 2.5rem; margin-bottom: 1.5rem; line-height: 1.2; animation: slideLeft 0.8s ease-out 0.2s both; color: #fff; }
    .mission-text p { font-size: 1.05rem; color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.8; animation: slideLeft 0.8s ease-out 0.3s both; }
    .mission-visual { position: relative; height: 400px; animation: slideRight 0.8s ease-out 0.2s both; }
    .morph-shape {
      position: absolute; width: 200px; height: 200px;
      background: linear-gradient(135deg, rgba(0, 217, 255, 0.3), rgba(74, 222, 128, 0.2));
      border: 2px solid rgba(0, 217, 255, 0.5);
      animation: morphShape 6s ease-in-out infinite;
    }
    .morph-shape:nth-child(1) { top: 20px; left: 50px; animation-delay: 0s; }
    .morph-shape:nth-child(2) { top: 150px; right: 50px; animation-delay: 1s; background: linear-gradient(135deg, rgba(74, 222, 128, 0.3), rgba(0, 217, 255, 0.2)); }
    .morph-shape:nth-child(3) { bottom: 20px; left: 100px; width: 150px; height: 150px; animation-delay: 2s; background: linear-gradient(135deg, rgba(255, 193, 7, 0.2), rgba(74, 222, 128, 0.2)); }

    /* Pillars */
    .pillars-section { padding: 6rem 0; background: linear-gradient(180deg, rgba(0, 217, 255, 0.05) 0%, transparent 100%); }
    .section-header { text-align: center; margin-bottom: 4rem; animation: fadeUp 0.8s ease-out 0.2s both; }
    .section-label { font-size: 0.85rem; color: var(--accent); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.5rem; font-weight: 600; }
    .section-header h2 { font-size: 2.5rem; margin-bottom: 1rem; color: #fff; }
    .section-header p { font-size: 1.05rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto; }
    .pillars-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; }
    .pillar {
      background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(74, 222, 128, 0.05) 100%);
      border: 1px solid rgba(0, 217, 255, 0.2); border-radius: 12px; padding: 2.5rem;
      position: relative; overflow: hidden; animation: fadeUp 0.8s ease-out forwards; opacity: 0; transition: all 0.3s;
    }
    .pillar:nth-child(1) { animation-delay: 0.2s; }
    .pillar:nth-child(2) { animation-delay: 0.3s; }
    .pillar:nth-child(3) { animation-delay: 0.4s; }
    .pillar:hover { transform: translateY(-8px); border-color: rgba(74, 222, 128, 0.5); background: linear-gradient(135deg, rgba(0, 217, 255, 0.15) 0%, rgba(74, 222, 128, 0.1) 100%); }
    .pillar-number { font-size: 3.5rem; font-weight: 700; background: linear-gradient(135deg, var(--primary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; opacity: 0.2; margin-bottom: 1rem; }
    .pillar-title { font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: var(--accent); }
    .pillar-description { font-size: 0.95rem; color: var(--text-secondary); line-height: 1.7; }

    /* Values Timeline */
    .values-section { padding: 6rem 0; }
    .timeline { position: relative; padding: 2rem 0; }
    .timeline::before { content: ''; position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, var(--primary), var(--accent), transparent); transform: translateX(-50%); }
    .timeline-item { margin-bottom: 3rem; width: 50%; animation: fadeUp 0.8s ease-out forwards; opacity: 0; }
    .timeline-item:nth-child(odd) { margin-left: 0; text-align: right; padding-right: 3rem; animation-delay: 0.2s; }
    .timeline-item:nth-child(even) { margin-left: auto; padding-left: 3rem; animation-delay: 0.3s; }
    .timeline-dot { position: absolute; left: 50%; top: 0; width: 16px; height: 16px; background: var(--bg-dark); border: 3px solid var(--accent); border-radius: 50%; transform: translateX(-50%); z-index: 2; }
    .timeline-content { background: rgba(0, 217, 255, 0.08); border: 1px solid rgba(0, 217, 255, 0.2); border-radius: 8px; padding: 2rem; position: relative; transition: all 0.3s; }
    .timeline-item:hover .timeline-content { background: rgba(0, 217, 255, 0.15); border-color: rgba(74, 222, 128, 0.4); transform: scale(1.05); }
    .timeline-title { font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--accent); }
    .timeline-description { font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; }

    /* Stats */
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-top: 3rem; padding: 2rem; background: rgba(0, 217, 255, 0.05); border-radius: 12px; }
    .stat-item { text-align: center; animation: scaleIn 0.6s ease-out forwards; opacity: 0; }
    .stat-item:nth-child(1) { animation-delay: 0.4s; }
    .stat-item:nth-child(2) { animation-delay: 0.5s; }
    .stat-item:nth-child(3) { animation-delay: 0.6s; }
    .stat-value { font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, var(--primary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stat-label { font-size: 0.9rem; color: var(--text-secondary); margin-top: 0.5rem; }

    /* CTA Section */
    .m-cta-section { padding: 6rem 0 10rem; text-align: center; position: relative; }
    .m-cta-section h2 { font-size: 2.5rem; margin-bottom: 1rem; animation: fadeUp 0.8s ease-out 0.2s both; color: #fff; }
    .m-cta-section p { font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto 2rem; animation: fadeUp 0.8s ease-out 0.3s both; }
    .cta-buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; animation: fadeUp 0.8s ease-out 0.4s both; }

    @media (max-width: 768px) {
      .mission-grid, .timeline::before { display: none; }
      .mission-text, .timeline-item { width: 100%; text-align: left !important; padding-right: 0 !important; padding-left: 0 !important; }
      .mission-hero h1 { font-size: 2rem; }
      .section-header h2 { font-size: 1.8rem; }
    }
  </style>

  <main>
    <!-- Hero Section -->
    <section class="mission-hero">
      <div class="hero-content">
        <h1>
          <span class="word">Drive</span>
          <span class="word">technology</span>
          <span class="word">forward</span>
          <span class="word">with</span>
          <span class="word">purpose</span>
        </h1>
        <p class="hero-description">We partner with visionary companies to architect, build, and scale solutions that transform businesses and create lasting impact in a rapidly evolving digital landscape.</p>
        <div class="hero-cta">
          <a href="mailto:contact@blazrs.com" class="m-btn m-btn-primary">Start your journey</a>
          <a href="salesforce.html" class="m-btn m-btn-secondary">Learn more</a>
        </div>
      </div>
    </section>

    <!-- Mission Section -->
    <section id="mission" class="mission-section">
      <div class="mission-container">
        <div class="mission-grid">
          <div class="mission-text">
            <h2>Why Blazrs exists</h2>
            <p>Great technology isn't built in isolation. It's born from deep understanding of your challenges, relentless focus on outcomes, and unwavering commitment to excellence.</p>
            <p>We don't just solve problems—we unlock potential. Every project is an opportunity to push boundaries and create something that matters.</p>
            <p>Your success is our obsession. When you grow, we grow. That alignment drives everything we do.</p>
          </div>
          <div class="mission-visual">
            <div class="morph-shape"></div>
            <div class="morph-shape"></div>
            <div class="morph-shape"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Pillars Section -->
    <section id="pillars" class="pillars-section">
      <div class="mission-container">
        <div class="section-header">
          <div class="section-label">How we operate</div>
          <h2>Three pillars of our approach</h2>
          <p>Every engagement is built on these core principles that guide our decisions and define our impact</p>
        </div>

        <div class="pillars-grid">
          <div class="pillar">
            <div class="pillar-number">01</div>
            <h3 class="pillar-title">Deep Expertise</h3>
            <p class="pillar-description">We don't outsource complexity. Our team brings 8+ years of battle-tested experience across Salesforce, marketing operations, AI, and enterprise technology. We know the landscape inside and out.</p>
          </div>

          <div class="pillar">
            <div class="pillar-number">02</div>
            <h3 class="pillar-title">Outcome-Driven</h3>
            <p class="pillar-description">Metrics matter. Every strategy is validated by data. Every implementation is measured. We're obsessed with results because your business depends on them.</p>
          </div>

          <div class="pillar">
            <div class="pillar-number">03</div>
            <h3 class="pillar-title">Partnership Mindset</h3>
            <p class="pillar-description">We're not vendors—we're partners invested in your success. Transparent communication, honest feedback, and radical accountability define how we work.</p>
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
            <div class="stat-label">SaaS companies served</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Timeline Section -->
    <section id="values" class="values-section">
      <div class="mission-container">
        <div class="section-header">
          <div class="section-label">What we believe in</div>
          <h2>Our values shape every interaction</h2>
          <p>These aren't words on a wall—they're how we operate, make decisions, and build relationships</p>
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Customer Obsession</h3>
              <p class="timeline-description">We begin every project by deeply understanding your business, market, and goals. Your challenges become our challenges. Your wins become our wins.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Radical Honesty</h3>
              <p class="timeline-description">We tell you what we think, not what you want to hear. If something won't work, we say so—and offer better alternatives. Trust is built on truth.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Relentless Quality</h3>
              <p class="timeline-description">Excellence isn't negotiable. From code to communication, we maintain uncompromising standards. Details matter because they compound.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3 class="timeline-title">Always Learning</h3>
              <p class="timeline-description">Technology evolves. So do we. We invest in staying ahead of trends, mastering new tools, and deepening our expertise so you benefit from cutting-edge knowledge.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="m-cta-section">
      <div class="mission-container">
        <h2>Ready to build something extraordinary?</h2>
        <p>Let's explore how we can drive your technology forward and unlock new possibilities for your organization</p>
        <div class="cta-buttons">
          <a href="mailto:contact@blazrs.com" class="m-btn m-btn-primary">Get in touch</a>
        </div>
      </div>
    </section>
  </main>
  
  <script>
    // Scroll animation for sections
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll('.fadeUp, .slideLeft, .slideRight, .scaleIn').forEach(el => {
          observer.observe(el);
        });
    });
  </script>
"""

# 3. Combine it into about.html
# Since the body background is dark in the user's code, we should ensure the body tag has the dark background styling
# In Blazrs, we can just apply a specific class to body, or since the CSS rules apply to body naturally, it's fine.
final_html = blazrs_header + user_code + blazrs_footer

# Wait! blazrs_header contains <body class="dark-theme"> or something?
# In index.html, it's just <body>.
# The user's css sets `body { background: var(--bg-dark); }`. This will make the whole page dark. Perfect.

with open('about.html', 'w') as f:
    f.write(final_html)
