from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import requests
import os.path


def parse_pages(url):
    html_page = requests.get(url)
    if html_page.status_code == 200:
        soup = BS(html_page.content, 'html.parser')
        for a in soup.find(attrs={"class": 'armsslide'}).find_all('a'):
            yield urljoin(url,  a.attrs['href'])
    else:
        print("Something went wront: " + html_page.status_code)


def parse_images(url):
    html_page = requests.get(url)
    soup = BS(html_page.content, 'html.parser')
    if html_page.status_code == 200:
        image_url = soup.find(attrs={"class": 'armstxt'}).find_all('img')
        for img in image_url:
            yield urljoin(url, img.attrs['src'])


def download_images(img_url):
    title = os.path.basename(img_url).lower()
    if("drosha" not in title and
            "gerbi" not in title):
        title = title[:-4] + "s_gerbi.jpg"
    print(f"downloading {title}...")
    file = open(title, "wb")
    file.write(requests.get(img_url).content)
    file.close()


link = 'http://www.heraldika.ge/index.php?m=85&p_news=1'
pages_generator = parse_pages(link)
for i in pages_generator:
    images_generator = parse_images(i)
    for j in images_generator:
        download_images(j)
