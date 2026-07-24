import re

html_file = 'salesforce.html'
with open(html_file, 'r') as f:
    content = f.read()

new_section = """<section class="salesforce">
    <div class="wrap">
      <div class="sf-grid">
        <div>
          <div class="sf-badge"><span></span> Full Clouds Coverage</div>
          <h2>One partner, across<br>the whole platform.</h2>
          <p class="sf-copy">Rather than handing off between vendors per cloud, our team carries context from
            discovery through go-live and beyond — across every corner of the Salesforce ecosystem you rely on.</p>
        </div>
      </div>
      
      <div class="sf-list">
        
        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Sales Cloud</h4>
            <p>Transform your sales organization with a scalable CRM platform designed to improve productivity, increase visibility, and accelerate revenue growth. We help businesses streamline every stage of the sales lifecycle—from lead capture and qualification to opportunity management, forecasting, and post-sale engagement.</p>
            <p>Our experts design intelligent sales processes using automation, AI-powered insights, and customized dashboards that give sales leaders complete visibility into pipeline health and team performance. We also implement advanced Configure, Price, Quote (CPQ) solutions tailored to your products and pricing models, enabling your teams to generate accurate quotes faster, reduce manual effort, and shorten sales cycles.</p>
            <p>Whether you're scaling a startup or optimizing a global sales organization, we build solutions that empower your sales teams to focus on building stronger customer relationships and closing more deals.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>Lead & Opportunity Management</li>
              <li>Sales Process Automation</li>
              <li>AI-Powered Forecasting & Pipeline Insights</li>
              <li>CPQ (Configure, Price, Quote) Implementation</li>
              <li>Territory & Account Planning</li>
              <li>Sales Dashboards & Performance Analytics</li>
            </ul>
          </div>
        </div>

        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Service Cloud</h4>
            <p>Deliver exceptional customer support with intelligent service operations that improve response times, increase agent productivity, and enhance customer satisfaction. We help organizations implement scalable service solutions that support customers across email, chat, phone, messaging, and self-service channels.</p>
            <p>From intelligent case routing and automated workflows to knowledge management and AI-assisted support, our solutions enable service teams to resolve issues faster while maintaining consistent customer experiences.</p>
            <p>We also build customer portals, service analytics, and automation frameworks that reduce operational costs while improving service quality.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>Intelligent Case Management</li>
              <li>Omnichannel Customer Support</li>
              <li>Knowledge Base & Self-Service Portals</li>
              <li>Workflow & Approval Automation</li>
              <li>Service Performance Dashboards</li>
              <li>AI-Assisted Customer Support</li>
            </ul>
          </div>
        </div>

        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Marketing Cloud</h4>
            <p>Create personalized customer experiences that strengthen relationships and drive measurable business growth. We help organizations design intelligent customer journeys that deliver relevant communications across email, SMS, push notifications, advertising, and digital channels.</p>
            <p>Using advanced audience segmentation, automation, dynamic content, and personalization technologies, we ensure every customer interaction is timely, meaningful, and data-driven.</p>
            <p>Our consultants optimize campaign performance through continuous testing, reporting, and journey optimization to maximize engagement, conversions, and customer lifetime value.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>Customer Journey Design</li>
              <li>Email & SMS Campaign Automation</li>
              <li>Audience Segmentation & Personalization</li>
              <li>AMPscript & Dynamic Content</li>
              <li>Marketing Analytics & Reporting</li>
              <li>Cross-Channel Campaign Orchestration</li>
            </ul>
          </div>
        </div>

        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Experience Cloud</h4>
            <p>Build modern digital experiences that connect customers, partners, suppliers, and employees through secure, collaborative portals. We create branded experiences that provide easy access to information, business processes, and customer services while maintaining enterprise-grade security.</p>
            <p>Whether you're launching a customer support portal, partner ecosystem, employee workspace, or community platform, we design scalable solutions that improve collaboration, reduce manual processes, and increase engagement.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>Customer & Partner Portals</li>
              <li>Employee Digital Workspaces</li>
              <li>Secure Authentication & Access Control</li>
              <li>Community Collaboration</li>
              <li>Knowledge Sharing Platforms</li>
              <li>Custom Experience Development</li>
            </ul>
          </div>
        </div>

        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Data Cloud</h4>
            <p>Turn disconnected enterprise data into a unified, trusted source of intelligence. We help businesses integrate data from CRM systems, ERP platforms, marketing tools, websites, mobile applications, and external sources to create complete customer profiles.</p>
            <p>Our data architecture and governance strategies ensure high-quality, real-time information that supports personalization, analytics, AI initiatives, and strategic decision-making across the organization.</p>
            <p>With a unified data foundation, your business gains the agility to deliver personalized experiences while improving operational efficiency and reporting accuracy.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>Customer 360 Data Unification</li>
              <li>Identity Resolution</li>
              <li>Data Integration & Harmonization</li>
              <li>Real-Time Customer Segmentation</li>
              <li>Enterprise Data Governance</li>
              <li>Analytics & Business Intelligence</li>
            </ul>
          </div>
        </div>

        <div class="sf-item large">
          <div class="sf-item-content">
            <h4>Agentforce & AI</h4>
            <p>Accelerate innovation with intelligent automation and enterprise AI solutions that improve productivity, enhance customer experiences, and support better business decisions. We help organizations implement AI-powered assistants, autonomous agents, and intelligent workflows that seamlessly integrate into existing business processes.</p>
            <p>From generative AI and conversational interfaces to predictive analytics and workflow automation, we build AI solutions designed for real-world business outcomes. Every implementation follows responsible AI principles with strong governance, security, and scalability.</p>
            <p>Our approach focuses on practical AI adoption—helping organizations automate repetitive tasks, empower employees, and deliver personalized customer experiences while maintaining trust and compliance.</p>
          </div>
          <div class="sf-item-capabilities">
            <h5>Key Capabilities</h5>
            <ul>
              <li>AI Agents & Intelligent Assistants</li>
              <li>Generative AI Integration</li>
              <li>Workflow & Process Automation</li>
              <li>Predictive Analytics & Insights</li>
              <li>Enterprise AI Governance</li>
              <li>Custom AI Solution Development</li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </section>"""

# Replace the salesforce section
content = re.sub(r'<section class="salesforce">.*?</section>', new_section, content, flags=re.DOTALL)

with open(html_file, 'w') as f:
    f.write(content)
