import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace the logo link
    content = content.replace(
        '<a href="index.html#about"><img class="logo-img" src="logos/Blazrs Logo.png" alt="Blazrs logo"></a>',
        '<a href="index.html#hero"><img class="logo-img" src="logos/Blazrs Logo.png" alt="Blazrs logo"></a>'
    )
    
    # If it's index.html, add the hero id
    if file == 'index.html':
        content = content.replace('<section class="hero">', '<section class="hero" id="hero">')
        
    with open(file, 'w') as f:
        f.write(content)
