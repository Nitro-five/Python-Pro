import os
import csv
from PIL import Image

'''
    Извлекает метаданные из изображений в каталоге и сохраняет их в CSV файл.

    Параметры:
        directory (str): Путь к каталогу с изображениями.
        csv_file (str): Путь к исходному CSV файлу.
'''


def save_metadata_to_csv(directory, csv_file):
    # Функция для проверки расширения файла
    def is_image_file(filename):
        return filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))

    # Получение списка файлов с изображениями
    image_files = list(filter(is_image_file, os.listdir(directory)))

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['filename', 'format', 'size', 'mode'])
        writer.writeheader()

        for image_file in image_files:
            image_path = os.path.join(directory, image_file)
            with Image.open(image_path) as img:
                metadata = {
                    'filename': image_file,
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode
                }
                writer.writerow(metadata)


# Тест
directory = '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/collecting_statistics_images/images'
csv_file = 'image_metadata.csv'
save_metadata_to_csv(directory, csv_file)
