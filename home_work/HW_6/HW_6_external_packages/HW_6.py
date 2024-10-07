import requests


def download_page(url: str, filename: str) -> None:
    """
    Загружает содержимое HTML-страницы по указанному URL и сохраняет его в текстовый файл.

    Параметры:
    url : str
        Адрес страницы, которую необходимо загрузить.
    filename : str
        Имя файла, в который будет сохранено содержимое страницы.

    Возвращает:
    None

    Исключения:
    raises requests.exceptions.HTTPError
        Если сервер отвечает ошибкой HTTP (404, 500).
    raises requests.exceptions.RequestException
        Для общих ошибок запроса (например, проблемы с подключением).
    raises Exception
        Для других непредвиденных ошибок.
    """
    try:
        # GET-запрос к URL
        response = requests.get(url)
        # Успешен ли запрос (код 200)
        response.raise_for_status()

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Страницу успешно загружено и сохранено в '{filename}'.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
    except Exception as err:
        print(f"Другая ошибка: {err}")


if __name__ == "__main__":
    url = input("Введите URL страницы для загрузки: ")
    # Название файла для сохранения
    filename = "downloaded_page.txt"
    download_page(url, filename)
