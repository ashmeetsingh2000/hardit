import os, urllib.request, re, sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Paths
top_dir = os.path.abspath(os.path.dirname(__file__))
html_path = os.path.join(top_dir, 'scraped_raw.html')
images_dir = os.path.join(top_dir, 'images')
audio_dir = os.path.join(top_dir, 'audio')

os.makedirs(images_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all image URLs (src or data-original)
img_urls = set(re.findall(r'(https?://[^\"\'>]+\.(?:png|jpg|jpeg|svg|webp|gif))', html))
# Find audio URLs
audio_urls = set(re.findall(r'src=[\"\'](https?://[^\"\']+\.(?:mp3|wav|ogg|m4a))[\"\']', html))

print('Found', len(img_urls), 'image URLs')
print('Found', len(audio_urls), 'audio URLs')

def download(url, dest_dir):
    try:
        filename = os.path.basename(url.split('?')[0])
        dest_path = os.path.join(dest_dir, filename)
        if os.path.exists(dest_path):
            print('Already exists:', filename)
            return
        print('Downloading', url)
        urllib.request.urlretrieve(url, dest_path)
        print('Saved to', dest_path)
    except Exception as e:
        print('Failed to download', url, ':', e)

for url in img_urls:
    download(url, images_dir)

for url in audio_urls:
    download(url, audio_dir)
