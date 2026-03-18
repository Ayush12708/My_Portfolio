import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Certification

def get_og_image(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try og:image
        og_img = soup.find('meta', property='og:image') or soup.find('meta', attrs={'name': 'og:image'})
        if og_img and og_img.get('content'):
            return og_img['content']
            
        # Try twitter:image
        twitter_img = soup.find('meta', attrs={'name': 'twitter:image'})
        if twitter_img and twitter_img.get('content'):
            return twitter_img['content']
            
        return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

for cert in Certification.objects.all():
    url = cert.credential_url
    if not url:
        print(f"Skipping {cert.title}: no URL")
        continue
        
    print(f"Processing {cert.title}...")
    
    # Handle Google Drive Links
    if "drive.google.com/file/d/" in url:
        file_id = url.split('/d/')[1].split('/')[0]
        image_url = f"https://drive.google.com/thumbnail?id={file_id}&sz=w800"
        cert.image_url = image_url
        cert.save()
        print(f"  -> Set Drive Thumbnail: {image_url}")
        continue
        
    # Attempt to scrape OG Image for others
    scraped_url = get_og_image(url)
    if scraped_url:
        cert.image_url = scraped_url
        cert.save()
        print(f"  -> Found OG Image: {scraped_url}")
    else:
        print(f"  -> No image found")

print("Done updating certificate images!")
