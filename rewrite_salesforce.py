import re

html_file = 'salesforce.html'
with open(html_file, 'r') as f:
    content = f.read()

# We need to replace everything inside <section class="salesforce"> ... </section>
# And we also need to append the dialog if it isn't already there.

new_section = """<section class="salesforce">
    <div class="wrap">
      <div class="sf-grid">
        <div>
          <div class="sf-badge"><span></span> Full Clouds Coverage</div>
          <h2>One partner, across<br>the whole platform.</h2>
          <p class="sf-copy">Rather than handing off between vendors per cloud, our team carries context from
            discovery through go-live and beyond — across every corner of the Salesforce ecosystem you rely on.</p>
        </div>
        <div class="sf-list">
          <div class="sf-item" onclick="openCloudModal('Sales Cloud', 'Supercharge your sales teams with advanced pipeline management, AI-driven forecasting, and automated territory design. We customize CPQ (Configure, Price, Quote) workflows tailored exactly to your unique sales motion, ensuring faster deal closures and maximized revenue growth.')">
            <h4>Sales Cloud</h4>
            <p>Supercharge your sales teams with advanced pipeline management...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Service Cloud', 'Deliver exceptional customer support with intelligent case routing, seamless omnichannel experiences, and robust knowledge management systems. We help you implement self-service portals and automated workflows that significantly shorten resolution times and boost customer satisfaction.')">
            <h4>Service Cloud</h4>
            <p>Deliver exceptional customer support with intelligent case routing...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Marketing Cloud', 'Craft highly personalized, data-driven customer journeys using Journey Builder and dynamic AMPscript. We design sophisticated segmentation strategies and cross-channel campaigns that engage your audience at the right time, driving higher conversions and brand loyalty.')">
            <h4>Marketing Cloud</h4>
            <p>Craft highly personalized, data-driven customer journeys...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Experience Cloud', 'Build immersive, branded digital portals that connect your customers, partners, and employees directly to your core Salesforce data. We create secure, collaborative communities that enhance engagement, streamline onboarding, and foster long-term relationships.')">
            <h4>Experience Cloud</h4>
            <p>Build immersive, branded digital portals that connect your customers...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Data Cloud', 'Break down data silos and build unified, 360-degree customer profiles. We help you harmonize fragmented data from across your organization into a single, actionable source of truth, enabling real-time personalization and deeper analytical insights.')">
            <h4>Data Cloud</h4>
            <p>Break down data silos and build unified, 360-degree customer profiles...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Agentforce', 'Step into the future with autonomous agents. Deploy intelligent, autonomous AI agents that handle complex tasks, orchestrate workflows, and augment your workforce at scale, stepping into the future of proactive and autonomous operations.')">
            <h4>Agentforce</h4>
            <p>Deploy intelligent, autonomous AI agents that handle complex tasks...</p>
          </div>
          <div class="sf-item" onclick="openCloudModal('Einstein AI', 'Embed predictive and generative AI natively into every workflow. We layer intelligent automation on top of a clean, well-governed data foundation to automate repetitive tasks, predict trends, and deliver proactive, intelligent experiences.')">
            <h4>Einstein AI</h4>
            <p>Embed predictive and generative AI natively into every workflow...</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

# Use regex to replace the section
content = re.sub(r'<section class="salesforce">.*?</section>', new_section, content, flags=re.DOTALL)

with open(html_file, 'w') as f:
    f.write(content)
