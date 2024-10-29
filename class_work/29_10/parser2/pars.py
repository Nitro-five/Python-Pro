import requests
from bs4 import BeautifulSoup
import json

# URL статьи на Bloomberg
url = 'https://www.bloomberg.com/news/articles/2024-10-29/microsoft-s-github-unit-cuts-ai-deals-with-google-anthropic'

# Устанавливаем User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Делаем запрос с заголовками
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверка на ошибки HTTP

    # Парсим страницу
    soup = BeautifulSoup(response.content, 'html.parser')

    # Выводим HTML-код страницы для проверки
    print(soup.prettify())

    # Извлекаем заголовок
    title = soup.find('h1').text.strip()

    # Извлекаем все параграфы
    paragraphs = soup.find_all('p')  # Извлекаем все параграфы
    content = [p.text.strip() for p in paragraphs]  # Извлекаем текст из всех параграфов

    # Создаем словарь для сохранения данных
    data = {
        'title': title,
        'content': content
    }

    # Сохраняем данные в файл JSON
    with open('bloomberg_article_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print("Данные успешно сохранены в файл bloomberg_article_data.json")

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")
