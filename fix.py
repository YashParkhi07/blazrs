html_file = 'salesforce.html'
with open(html_file, 'r') as f:
    content = f.read()

import re

# Remove the flashcard-grid entirely
content = re.sub(r'<div class="flashcard-grid">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# Let's just find the end of sf-grid's left column and insert sf-list
left_col_end = content.find('</div>\s*</div>') # This is risky. Let's just manually replace using python logic.
