import re

html_file = 'salesforce.html'
with open(html_file, 'r') as f:
    content = f.read()

# We want to replace everything from <div class="flashcard-grid"> to the end of that div
# with the new sf-list

sf_list = """
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
"""

# Replace flashcard-grid with sf-list
# Note: we also need to put it back inside sf-grid!

pattern = re.compile(r'</div>\s*</div>\s*<div class="flashcard-grid">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
content = pattern.sub(sf_list + '\n      </div>', content)

# Add the dialog at the bottom, before closing body tag
dialog_html = """
  <dialog id="cloud-dialog" class="cloud-dialog">
    <div class="dialog-content">
      <h3 id="dialog-title">Cloud Name</h3>
      <p id="dialog-desc">Cloud description</p>
      <button onclick="document.getElementById('cloud-dialog').close()">Close</button>
    </div>
  </dialog>

  <script>
    function openCloudModal(title, desc) {
      document.getElementById('dialog-title').innerText = title;
      document.getElementById('dialog-desc').innerText = desc;
      document.getElementById('cloud-dialog').showModal();
    }
    
    // Light dismiss
    const dialog = document.getElementById('cloud-dialog');
    dialog.addEventListener('click', (e) => {
      const dialogDimensions = dialog.getBoundingClientRect()
      if (
        e.clientX < dialogDimensions.left ||
        e.clientX > dialogDimensions.right ||
        e.clientY < dialogDimensions.top ||
        e.clientY > dialogDimensions.bottom
      ) {
        dialog.close()
      }
    });
  </script>
"""

content = content.replace('</body>', dialog_html + '\n</body>')

with open(html_file, 'w') as f:
    f.write(content)

