import urllib.request
import re
from bs4 import BeautifulSoup
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scraped_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

recs = soup.find_all('div', class_=re.compile(r't-rec'))

print(f'Total rec blocks: {len(recs)}')

for i, r in enumerate(recs):
    rec_id = r.get('id', '')
    rec_type = r.get('data-record-type', '')
    screen_max = r.get('data-screen-max', '')
    
    text_content = r.get_text(separator=' ', strip=True)
    
    block_imgs = []
    for img in r.find_all('img'):
        src = img.get('data-original') or img.get('src')
        if src and src not in block_imgs: 
            block_imgs.append(src)
    
    zero_elems = []
    if rec_type == '396':
        for elem in r.find_all('div', class_=re.compile(r'tn-elem')):
            elem_id = elem.get('data-elem-id', '')
            elem_type = elem.get('data-elem-type', '')
            elem_text = elem.get_text(strip=True)
            elem_img = elem.find('img')
            img_src = elem_img.get('data-original') if elem_img else None
            zero_elems.append({
                'id': elem_id,
                'type': elem_type,
                'text': elem_text,
                'img': img_src
            })

    print(f"\n--- [{i+1}] Block ID: {rec_id} | Type: {rec_type} | ScreenMax: {screen_max} ---")
    print(f"Text: {text_content[:200]}..." if len(text_content) > 200 else f"Text: {text_content}")
    print(f"Images count: {len(block_imgs)}")
    for img in block_imgs:
        print(f"   Image: {img}")
    if zero_elems:
        print(f"Zero elements ({len(zero_elems)}):")
        for ze in zero_elems:
            print(f"   - Elem {ze['id']} ({ze['type']}): text='{ze['text']}', img='{ze['img']}'")
