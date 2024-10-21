import http.server
import socketserver
import threading

PORT = 8080


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    Обработчик запросов для веб-сервера.

    Отвечает на GET-запросы, возвращая простое текстовое сообщение.
    """

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello world , web-server\n".encode('utf-8'))


def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    """
    Запускает веб-сервер, который обслуживает клиентов в новых потоках.

    Аргументы:
    server_class -- класс сервера (по умолчанию HTTPServer).
    handler_class -- класс обработчика запросов (по умолчанию MyHandler).
    """
    with server_class(("", PORT), handler_class) as httpd:
        print(f"Сервер запущен на порту {PORT}...")
        httpd.serve_forever()


if __name__ == "__main__":
    # Запуск сервера в отдельных потоках
    for _ in range(4):  # Создаем 4 потока
        thread = threading.Thread(target=run)
        thread.start()  # Запускаем новый поток
