import urllib.request
import re
import json
from bs4 import BeautifulSoup

url = 'https://webgency.tilda.ws/template5'
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

with open('scraped_raw.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Saved raw HTML, length:', len(html))

soup = BeautifulSoup(html, 'html.parser')

# Find all blocks (recs)
recs = soup.find_all('div', class_=re.compile(r't-rec'))
print(f'Total rec blocks: {len(recs)}')

for r in recs:
    rec_id = r.get('id', '')
    rec_type = r.get('data-record-type', '')
    print(f'Block ID: {rec_id}, Type: {rec_type}')

# Extract all image URLs
images = set()
for img in soup.find_all('img'):
    if img.get('src'): images.add(img['src'])
    if img.get('data-original'): images.add(img['data-original'])

# Extract inline styles and background images
bg_images = set(re.findall(r'url\([\'\"]?(https://[^\'\"\)]+)[\'\"]?\)', html))

print('\nImages found:', len(images))
for img in list(images)[:10]:
    print(' -', img)

print('\nBackground images found:', len(bg_images))
for bg in bg_images:
    print(' -', bg)

# Audio / Video sources
media = set(re.findall(r'src=[\'\"](https?://[^\'\"]+\.(?:mp3|mp4|wav|ogg|webm))[\'\"]', html))
print('\nMedia found:', media)

# Extract custom font faces if any
fonts = set(re.findall(r'@font-face\s*\{[^}]+\}', html))
print('\nFonts defined:', len(fonts))

# Also fetch project CSS to find loaded fonts and styles
css_urls = re.findall(r'href=[\'\"](https://[^\'\"]+\.css[^\'\"]*)[\'\"]', html)
print('\nCSS Files:', css_urls)
