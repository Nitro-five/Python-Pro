from concurrent.futures import ThreadPoolExecutor
import os
from PIL import Image


def img_update_size(image_path, output_size):
    """
    Изменяет размер изображения и сохраняет его с новым именем.

    Параметры:
    image_path : str
        Путь к изображению, которое нужно изменить.
    output_size : tuple
        Новый размер изображения (ширина, высота).
    """
    try:
        # Открываем изображение по указанному пути
        with Image.open(image_path) as img:
            # Изменяем размер изображения
            img_resize = img.resize(output_size)
            # Получаем базовое имя файла
            base_name = os.path.basename(image_path)
            # Создаем новое имя для сохранения измененного изображения
            new_name = f'resized_{base_name}'
            # Сохраняем измененное изображение
            img_resize.save(new_name)
            print(f'Обработан {new_name}')
    except Exception as ex:
        # Обрабатываем ошибки и выводим сообщение
        print(f'Ошибка при работе с {image_path}: {ex}')


# Список изображений для обработки
image_paths = [
    '/Users/admin/Desktop/Photos/633529.JPG',
    '/Users/admin/Desktop/Photos/633530.JPG',
    '/Users/admin/Desktop/Photos/IMG_0115.WEBP'
]

# Новый размер для изображений
output_size = (800, 600)  # Ширина 800 пикселей, высота 600 пикселей

# Создаем пул потоков для обработки изображений
with ThreadPoolExecutor() as executor:
    # Запускаем обработку изображений параллельно
    executor.map(img_update_size, image_paths, [output_size] * len(image_paths))
