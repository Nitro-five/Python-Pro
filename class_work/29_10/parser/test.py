import requests
from bs4 import BeautifulSoup
import os

url = "https://ru.wikipedia.org/wiki/Volkswagen"
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    title = soup.title.string

    print("Название страницы:", title)

    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        print(header.get_text())

    for paragraph in soup.find_all('p'):
        print(paragraph.get_text())

    if not os.path.exists('images'):
        os.makedirs('images')

    images = []
    for img in soup.find_all('img'):
        img_url = img['src']
        if img_url.startswith('//'):
            full_img_url = 'https:' + img_url
        elif img_url.startswith('http://') or img_url.startswith('https://'):
            full_img_url = img_url
        else:
            continue

        images.append(full_img_url)

        img_response = requests.get(full_img_url)
        if img_response.status_code == 200:
            img_name = os.path.join('images', os.path.basename(img_url))
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
            print(f"Скачано: {img_name}")
        else:
            print(f"Ошибка при скачивании изображения: {full_img_url}")

    print(f"Найдено изображений: {len(images)}")
else:
    print("Ошибка при запросе страницы:", response.status_code)
