import requests
import unittest


class WebService:
    """
    Класс для получения данных с веб-сайта.
    """

    def get_data(self, url: str) -> dict:
        """
        Выполняет GET-запрос к указанному URL и возвращает JSON-ответ.

        return: JSON-ответ как словарь
        """
        response = requests.get(url)
        # Поднимает ошибку для статусов 4xx/5xx
        response.raise_for_status()
        return response.json()


from unittest.mock import patch, Mock


class TestWebService(unittest.TestCase):
    """
    Тести для класу WebService.
    """

    """
    @patch('requests.get') из библиотеки unittest.mock используется 
    для замены метода requests.get на его мок-объект во время выполнения теста
    """

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        """
        Тестирование метода get_data на успешный запрос (статус 200).
        """
        # фейк ответ 200
        mock_response = Mock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data('http://test.com')

        # Тест
        mock_get.assert_called_once_with('http://test.com')
        # Проверка результата
        self.assertEqual(result, {"data": "test"})

    @patch('requests.get')
    def test_get_data_not_found(self, mock_get):
        """
        Тестирование метода get_data на запрос (404).
        """
        # фейк ответ 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("Not Found")
        mock_get.return_value = mock_response

        service = WebService()

        # Ошибка
        with self.assertRaises(requests.HTTPError):
            service.get_data('http://test.com/notfound')

    @patch('requests.get')
    def test_get_data_server_error(self, mock_get):
        # Фейк ответ для 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError("Server Error")
        mock_get.return_value = mock_response

        service = WebService()

        # Ошибка
        with self.assertRaises(requests.HTTPError):
            service.get_data('http://test.com/servererror')


if __name__ == "__main__":
    unittest.main()
