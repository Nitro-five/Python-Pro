import  threading
import requests
import time


def download_file_url(url):
    '''
    Функцию выполняет GET запрос для получения содержимого файла по указаному URL.
    '''
    start_time = time.time()

    try:
        # GET запрос
        response = requests.get(url)
        response.raise_for_status()
        file_name = url.split('/')[-1]

        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f'Скачено {file_name}')
    except Exception as ex:
        print(f'Ошибка при работе с {url}: {ex}')

    end_time = time.time()
    exe_time = end_time - start_time
    print(f'Время исполнения {file_name}: {exe_time:.4f} секунд')

#Список интересующих файлов URL

urls = [
    'https://i.pinimg.com/736x/0c/ca/82/0cca826d5fc46ec284aa3dfc89490e79.jpg',
    'https://media.infopay.net/thumbnails/53fTc2fDOiUVkfjVqxcH1JRGzFNEaIsVX73AHcpa.webp',
    'https://jdmgame.com/wp-content/uploads/2023/10/4-scaled.jpg'
]

threads = []
for url in urls:
    thread = threading.Thread(target=download_file_url, args=(url,))
    threads.append(thread)
    thread.start()

    active_threads = threading.active_count()
    print(f'Активные потоки: {active_threads - 1}')

for thread in threads:
    thread.join()

print('Файлы загружены')