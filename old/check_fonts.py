import urllib.request
import re
import os
from bs4 import BeautifulSoup

with open('scraped_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for webfont links or font imports in HTML
font_links = re.findall(r'href=[\'\"]([^\'\"]+fonts[^\'\"]*)[\'\"]', html)
print('Font links in HTML:', font_links)

# Scan project_blocks.css for font-face
if os.path.exists('project_blocks.css'):
    with open('project_blocks.css', 'r', encoding='utf-8') as f:
        css = f.read()
    ffs = re.findall(r'@font-face\s*\{[^}]+\}', css)
    print(f'Font faces in project_blocks.css: {len(ffs)}')
    for ff in ffs:
        print(' -', ff)

# Let's check all CSS files in HTML
css_urls = re.findall(r'href=[\'\"](https://static\.tildacdn\.net/[^\'\"]+\.css[^\'\"]*)[\'\"]', html)
for url in css_urls:
    try:
        content = urllib.request.urlopen(url).read().decode('utf-8')
        ffs = re.findall(r'@font-face\s*\{[^}]+\}', content)
        if ffs:
            print(f'Found @font-face in {url}:', ffs)
        # Check font-family declarations
        f_fams = set(re.findall(r'font-family\s*:\s*([^;\}]+)', content))
        if f_fams:
            print(f'Font families in {url}:', f_fams)
    except Exception as e:
        print('Err reading CSS:', url, e)
