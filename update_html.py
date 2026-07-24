import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to replace src="something.png" with src="logos/something.png"
    # But only if it doesn't already have logos/
    
    content = re.sub(r'src="([^"]+\.png)"', r'src="logos/\1"', content)
    
    with open(file, 'w') as f:
        f.write(content)
