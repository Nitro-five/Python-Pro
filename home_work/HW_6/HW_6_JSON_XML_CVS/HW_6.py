import csv
import json
import xml.etree.ElementTree as ET


class CSVtoJSONConverter:
    @staticmethod
    def convert(csv_file_path: str, json_file_path: str) -> None:
        """
        Конвертирует CSV-файл в JSON.

        Параметры:
        csv_file_path : str
            Путь к CSV-файлу для чтения.
        json_file_path : str
            Путь к JSON-файлу для записи.
        """
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            # Читаем CSV как словарь
            csv_reader = csv.DictReader(csv_file)
            # Собираем данные в список
            data = [row for row in csv_reader]

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            # Записываем данные в JSON
            json.dump(data, json_file, indent=4)


class JSONtoCSVConverter:
    @staticmethod
    def convert(json_file_path: str, csv_file_path: str) -> None:
        """
        Конвертирует JSON-файл в CSV.

        Параметры:
        json_file_path : str
            Путь к JSON-файлу для чтения.
        csv_file_path : str
            Путь к CSV-файлу для записи.
        """
        with open(json_file_path, mode='r', encoding='utf-8') as json_file:
            # Загружаем данные из JSON
            data = json.load(json_file)

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # Создаем писателя CSV
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            # Записываем данные
            csv_writer.writerows(data)


class XMLtoJSONConverter:
    @staticmethod
    def convert(xml_file_path: str, json_file_path: str) -> None:
        """
        Конвертирует XML-файл в JSON.

        Параметры:
        xml_file_path : str
            Путь к XML-файлу для чтения.
        json_file_path : str
            Путь к JSON-файлу для записи.
        """
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        def parse_element(element):
            data = {}
            for child in element:
                data[child.tag] = parse_element(child) if len(child) > 0 else child.text
            return data

        data = parse_element(root)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    # Конвертация CSV в JSON
    csv_file_path = '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_6/HW_6_csv_file/students.csv'
    json_file_path_from_csv = 'test.json'
    CSVtoJSONConverter.convert(csv_file_path, json_file_path_from_csv)
    print(f"Конвертация {csv_file_path} в {json_file_path_from_csv} завершена.")
