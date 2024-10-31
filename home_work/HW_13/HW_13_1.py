import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta


def get_page(url):
    """ Получаем HTML-страницу по URL. """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Ошибка при получении страницы: {e}")
        return None


def parse_news(soup):
    """ Извлекаем новости из HTML-кода. """
    # Список для хранения новостей
    news_list = []
    if soup is None:
        # Если нет HTML, возвращаем пустой список
        return news_list
        # Находим все статьи
    articles = soup.find_all('li', class_='stream-item')
    for article in articles:
        # Ищем заголовок
        title_tag = article.find('h3', class_='stream-item-title')
        # Получаем текст заголовка
        title = title_tag.get_text(strip=True) if title_tag else "Нет заголовка"
        # Получаем ссылку
        link = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else None
        if link and not link.startswith('http'):
            # Добавляем базовый URL, если нужно
            link = 'https://news.yahoo.com' + link
        # Получаем время публикации
        publish_time = get_publish_time(link)

        # Преобразуем время публикации в дату
        if publish_time != "Нет времени публикации":
            # Убираем 'Z' и преобразуем в дату
            publish_date = datetime.fromisoformat(publish_time[:-1])
        else:
            publish_date = None

        # Проверяем, новость за последние 7 дней
        if publish_date and publish_date >= datetime.now() - timedelta(days=7):
            summary_tag = article.find('p', class_='finance-ticker-fetch-success_D(n)')
            summary = summary_tag.get_text(strip=True) if summary_tag else "Нет описания"

            # Добавляем новость в список
            news_list.append({
                'title': title,
                'link': link,
                'publish_time': publish_time,
                'summary': summary,
                'publish_date': publish_date
            })

            print(f"Обработано: {link}")

    return news_list


def get_publish_time(link):
    """ Получаем время публикации из статьи по ссылке. """
    if not link:
        return "Нет времени публикации"

    try:
        # Загружаем статью
        article_soup = get_page(link)
        time_tag = article_soup.find('time')
        if time_tag and time_tag.has_attr('datetime'):
            return time_tag['datetime']
    except Exception as e:
        print(f"Ошибка при получении времени публикации из {link}: {e}")

    return "Нет времени публикации"


def save_to_csv(data):
    """ Сохраняем данные о новостях в CSV файл. """
    # Создаем DataFrame из списка новостей
    df = pd.DataFrame(data)
    df.to_csv('news.csv', index=False, sep=';', encoding='utf-8-sig')
    print("Данные сохранены в news.csv")

    # Статистика по дням
    if not df.empty:
        # Преобразуем даты
        df['publish_date'] = pd.to_datetime(df['publish_date'])
        # Считаем количество публикаций по датам
        stats = df['publish_date'].dt.date.value_counts().sort_index()
        print("\nСтатистика публикаций по дням:")
        print(stats)


def main():
    """ Основная функция программы. """
    url = 'https://news.yahoo.com/?utm_source=vsesmi_online'
    soup = get_page(url)
    news_data = parse_news(soup)
    save_to_csv(news_data)


if __name__ == '__main__':
    main()
