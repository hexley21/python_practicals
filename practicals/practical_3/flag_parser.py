from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import requests
import unidecode  # pip install unidecode


def parse_pages(url):
    html_page = requests.get(url)
    if html_page.status_code == 200:
        soup = BS(html_page.content, 'html.parser')
        for a in soup.find(attrs={"class": 'armsslide'}).find_all('a'):
            yield urljoin(url,  a.attrs['href'])
    else:
        print(f"Something went wront: status code #{html_page.status_code}")


def parse_images(url):
    html_page = requests.get(url)
    soup = BS(html_page.content, 'html.parser')
    image_url = soup.find(attrs={"class": 'armstxt'}).find_all('img')
    for img in image_url:
        yield urljoin(url, img.attrs['src'])


def parse_titles(url):
    html_page = requests.get(url)
    soup = BS(html_page.content, 'html.parser')
    title_url = soup.find(attrs={"class": 'armstxt'}).find_all('td')
    for count, title in enumerate(title_url):
        if (count+1) % 2 == 0:
            start = str(title).find('>') + 2
            stop = str(title)[start:].find('<')
            yield str(title)[start-1:stop + start].replace("<br/>", "") \
                .replace(":", "").replace(" - ", " ").strip()


def download_images(img_url, titles):
    print(f"downloading {titles}...")
    title = str(unidecode.unidecode(titles)).replace(" ", "_") \
        .replace("-", "_").replace("`", "").replace("\'", "")
    file = open(title + ".jpg", "wb")
    file.write(requests.get(img_url).content)
    file.close()


link = 'http://www.heraldika.ge/index.php?m=85&p_news=1'
pages_generator = parse_pages(link)
for i in pages_generator:
    title_generator = parse_titles(i)
    images_generator = parse_images(i)
    for j, k in zip(images_generator, title_generator):
        download_images(j, k)
