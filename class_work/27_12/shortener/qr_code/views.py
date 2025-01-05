import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from links.models import Link


def generate_qr(request, short_url):
    """
    Генерирует QR-код для указанной короткой ссылки.

    Параметры:
    - request: HTTP-запрос, переданный в представление.
    - short_url: короткая ссылка, для которой необходимо создать QR-код.

    Возвращает:
    - HTTP-ответ с изображением QR-кода в формате PNG.
    """
    # Получаем объект Link по короткой ссылке
    link = get_object_or_404(Link, short_url=short_url)

    # Генерация QR-кода для оригинального URL
    qr = qrcode.make(link.original_url)

    # Сохраняем QR-код в буфер
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)

    # Возвращаем изображение QR-кода в HTTP-ответе
    return HttpResponse(buffer, content_type="image/png")
