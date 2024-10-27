import re

def delete_html_text(text):
    """
    Удаляет все HTML-теги из предоставленного текста.

    Аргументы:
    text (str): Текст, из которого нужно удалить HTML-теги.

    Возвращает:
    str: Текст без HTML-тегов.
    """
    template = r'<.*?>'
    return re.sub(template, '', text)

text = (' <p>This is a <strong>sample</strong> paragraph that demonstrates how HTML works.'
        '</p> <p>Here is a link to <a href="https://www.example.com">Example Website</a>.</p>')

print(delete_html_text(text))