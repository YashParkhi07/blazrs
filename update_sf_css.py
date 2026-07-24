import re

css_file = 'styles.css'
with open(css_file, 'r') as f:
    content = f.read()

# Replace .sf-grid and .sf-list with new styles
# It's easier to find the block from .sf-grid to .sf-item p and replace it all

pattern = r'\.sf-grid \{.*?\.sf-item p \{.*?\}'
new_css = """    .sf-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 32px;
      text-align: center;
      margin-bottom: 40px;
    }

    .sf-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 12.5px;
      color: #00A1E0;
      border: 1px solid rgba(0, 161, 224, 0.35);
      background: rgba(0, 161, 224, 0.08);
      padding: 7px 14px;
      border-radius: 999px;
      margin-bottom: 20px;
    }

    .sf-badge span {
      width: 7px;
      height: 7px;
      background: #00A1E0;
      border-radius: 50%;
    }

    .salesforce h2 {
      font-size: clamp(28px, 3.6vw, 42px);
      color: var(--paper);
      max-width: 15ch;
      margin: 0 auto;
    }

    .salesforce .sf-copy {
      font-size: 15px;
      color: var(--grey);
      max-width: 46ch;
      margin: 16px auto 0;
    }

    .sf-list {
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .sf-item.large {
      display: grid;
      grid-template-columns: 1.6fr 1fr;
      gap: 32px;
      align-items: stretch;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 32px;
      text-align: left;
    }

    .sf-item-content h4 {
      font-size: 24px;
      color: var(--cyan);
      margin-bottom: 16px;
      font-weight: 600;
    }

    .sf-item-content p {
      font-size: 14px;
      color: var(--grey);
      line-height: 1.6;
      margin-bottom: 16px;
    }

    .sf-item-content p:last-child {
      margin-bottom: 0;
    }

    .sf-item-capabilities {
      background: rgba(0, 161, 224, 0.05);
      border: 1px solid rgba(0, 161, 224, 0.2);
      border-radius: 8px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .sf-item-capabilities h5 {
      color: var(--paper);
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
      font-weight: 600;
    }

    .sf-item-capabilities ul {
      list-style-type: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .sf-item-capabilities li {
      font-size: 13.5px;
      color: var(--grey);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .sf-item-capabilities li::before {
      content: "✓";
      color: var(--cyan);
      font-weight: bold;
    }"""

content = re.sub(pattern, new_css, content, flags=re.DOTALL)

with open(css_file, 'w') as f:
    f.write(content)
