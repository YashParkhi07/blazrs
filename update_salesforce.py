import re

with open("salesforce.html", "r") as f:
    content = f.read()

# The user's code starts at <section class="pricing-section"> and ends at </section>
# I will replace it using regex.

new_html = """
      <div class="sf-grid" style="margin-top: 80px;">
        <div>
          <div class="sf-badge" style="background: rgba(0,161,224,0.1); color: var(--cyan);"><span style="background: var(--cyan);"></span> OUR SERVICES</div>
          <h2>Choose the right level of transformation</h2>
          <p class="sf-copy">From Salesforce implementation to enterprise-scale customer engagement transformation, choose the approach that fits your goals.</p>
        </div>
      </div>
      
      <!-- Horizontal Pricing Cards -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 40px; margin-bottom: 80px;">
        
        <!-- Ignite -->
        <div style="background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 40px 24px; display: flex; flex-direction: column; transition: transform 0.3s ease;">
          <p style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: var(--grey); margin-bottom: 12px;">01</p>
          <h4 style="font-size: 26px; color: var(--paper); margin-bottom: 4px; font-weight: 600;">Ignite</h4>
          <p style="font-size: 14px; color: var(--grey); margin-bottom: 24px;">Start your Salesforce journey</p>
          
          <p style="font-size: 32px; font-weight: 700; color: var(--cyan); margin-bottom: 20px;">$5K+<span style="font-size: 16px; color: var(--grey); font-weight: 400;"> / project</span></p>
          <p style="font-size: 14.5px; color: var(--grey); line-height: 1.6; margin-bottom: 32px; flex-grow: 1;">Build a strong Salesforce Marketing Cloud foundation and launch your first customer engagement initiatives.</p>
          
          <div style="border-top: 1px solid var(--line); padding-top: 24px; margin-bottom: 30px;">
            <ul style="list-style: none; padding: 0; color: var(--paper); font-size: 14px; display: flex; flex-direction: column; gap: 12px;">
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> SFMC environment setup</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Data Extensions & data model</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Email & template setup</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Automation Studio</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Journey Builder</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Basic personalization</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Testing & deployment</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Knowledge transfer</li>
            </ul>
          </div>
          <a href="#cta" style="display: block; text-align: center; padding: 12px; border: 1px solid var(--line); border-radius: 8px; text-decoration: none; color: var(--paper); font-weight: 600; transition: all 0.2s;">Get Started →</a>
        </div>

        <!-- Elevate -->
        <div style="background: var(--paper); border: 1px solid var(--paper); border-radius: 12px; padding: 40px 24px; display: flex; flex-direction: column; transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); position: relative;">
          <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: var(--cyan); color: #fff; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; padding: 6px 16px; border-radius: 20px;">Most Popular</div>
          <p style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: rgba(255,255,255,0.5); margin-bottom: 12px;">02</p>
          <h4 style="font-size: 26px; color: #fff; margin-bottom: 4px; font-weight: 600;">Elevate</h4>
          <p style="font-size: 14px; color: rgba(255,255,255,0.7); margin-bottom: 24px;">Optimize and scale</p>
          
          <p style="font-size: 32px; font-weight: 700; color: var(--cyan); margin-bottom: 20px;">$15K+<span style="font-size: 16px; color: rgba(255,255,255,0.5); font-weight: 400;"> / project</span></p>
          <p style="font-size: 14.5px; color: rgba(255,255,255,0.7); line-height: 1.6; margin-bottom: 32px; flex-grow: 1;">Scale your marketing operations with advanced automation, personalization and Salesforce integrations.</p>
          
          <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; margin-bottom: 30px;">
            <ul style="list-style: none; padding: 0; color: #fff; font-size: 14px; display: flex; flex-direction: column; gap: 12px;">
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Everything in Ignite</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Advanced Journey Builder</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Advanced segmentation</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> SQL & automation optimization</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> AMPscript & SSJS</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Salesforce CRM integration</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> API integrations</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> CloudPages</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Deliverability optimization</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Architecture & governance</li>
            </ul>
          </div>
          <a href="#cta" style="display: block; text-align: center; padding: 12px; background: var(--cyan); color: #fff; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;">Start Your Transformation →</a>
        </div>

        <!-- Accelerate -->
        <div style="background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 40px 24px; display: flex; flex-direction: column; transition: transform 0.3s ease;">
          <p style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: var(--grey); margin-bottom: 12px;">03</p>
          <h4 style="font-size: 26px; color: var(--paper); margin-bottom: 4px; font-weight: 600;">Accelerate</h4>
          <p style="font-size: 14px; color: var(--grey); margin-bottom: 24px;">Transform customer engagement</p>
          
          <p style="font-size: 32px; font-weight: 700; color: var(--cyan); margin-bottom: 20px;">$30K+<span style="font-size: 16px; color: var(--grey); font-weight: 400;"> / project</span></p>
          <p style="font-size: 14.5px; color: var(--grey); line-height: 1.6; margin-bottom: 32px; flex-grow: 1;">Create a connected customer engagement ecosystem across Marketing Cloud, Data Cloud and next-gen marketing.</p>
          
          <div style="border-top: 1px solid var(--line); padding-top: 24px; margin-bottom: 30px;">
            <ul style="list-style: none; padding: 0; color: var(--paper); font-size: 14px; display: flex; flex-direction: column; gap: 12px;">
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Everything in Elevate</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Data Cloud architecture</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Customer identity resolution</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Unified customer profiles</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Advanced data ingestion</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Real-time segmentation</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Cross-channel activation</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Marketing Cloud Next</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> AI-powered personalization</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Advanced integrations</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> 90-day post-launch support</li>
            </ul>
          </div>
          <a href="#cta" style="display: block; text-align: center; padding: 12px; border: 1px solid var(--line); border-radius: 8px; text-decoration: none; color: var(--paper); font-weight: 600; transition: all 0.2s;">Transform With Us →</a>
        </div>

        <!-- Apex -->
        <div style="background: var(--paper); border: 1px solid var(--paper); border-radius: 12px; padding: 40px 24px; display: flex; flex-direction: column; transition: transform 0.3s ease;">
          <p style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: rgba(255,255,255,0.5); margin-bottom: 12px;">04</p>
          <h4 style="font-size: 26px; color: #fff; margin-bottom: 4px; font-weight: 600;">Apex</h4>
          <p style="font-size: 14px; color: rgba(255,255,255,0.7); margin-bottom: 24px;">Enterprise-scale transformation</p>
          
          <p style="font-size: 32px; font-weight: 700; color: #fff; margin-bottom: 20px;">Custom</p>
          <p style="font-size: 14.5px; color: rgba(255,255,255,0.7); line-height: 1.6; margin-bottom: 32px; flex-grow: 1;">A dedicated Salesforce engineering and architecture team designed around your organization\'s long-term transformation.</p>
          
          <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; margin-bottom: 30px;">
            <ul style="list-style: none; padding: 0; color: #fff; font-size: 14px; display: flex; flex-direction: column; gap: 12px;">
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Everything in Accelerate</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Dedicated Solution Architect</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Salesforce Developers</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Data Cloud specialists</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Integration engineers</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Dedicated QA</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Delivery management</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Proactive monitoring</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Release management</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Technical governance</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Strategic roadmap</li>
              <li><span style="color: var(--cyan); margin-right: 8px;">✓</span> Custom SLA</li>
            </ul>
          </div>
          <a href="#cta" style="display: block; text-align: center; padding: 12px; border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; text-decoration: none; color: #fff; font-weight: 600; transition: all 0.2s;">Talk to an Architect →</a>
        </div>

      </div>
"""

pattern = r'<section class="pricing-section">.*?</section>'
new_content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open("salesforce.html", "w") as f:
    f.write(new_content)
