class MessageSender:
    def send_message(self, message: str):
        """
        Абстрактный метод для отправки сообщения.

        Параметры:
        message : str
            Текст сообщения для отправки.
        """
        pass


class SMSService:
    def send_sms(self, phone_number: str, message: str) -> None:
        """
        Отправляет SMS-сообщение.
        """
        print(f"Отправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address: str, message: str) -> None:
        """
        Отправляет электронное письмо.
        """
        print(f"Отправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id: str, message: str) -> None:
        """
        Отправляет Push-уведомление.
        """
        print(f"Отправка Push уведомления на {device_id}: {message}")


# Адаптеры
class SMSAdapter(MessageSender):
    def __init__(self, sms_service: SMSService):
        """
        Инициализирует адаптер для отправки SMS.

        Параметры:
        sms_service : SMSService
            Экземпляр сервиса для отправки SMS.
        """
        self.sms_service = sms_service

    def send_message(self, message: str, recipient: str) -> None:
        """
        Отправляет SMS-сообщение через адаптированный сервис.

        Параметры:
        message : str
            Текст сообщения для отправки.
        recipient : str
            Номер телефона получателя.
        """
        self.sms_service.send_sms(recipient, message)


class EmailAdapter(MessageSender):
    def __init__(self, email_service: EmailService):
        """
        Инициализирует адаптер для отправки Email.

        Параметры:
        email_service : EmailService
            Экземпляр сервиса для отправки Email.
        """
        self.email_service = email_service

    def send_message(self, message: str, recipient: str) -> None:
        """
        Отправляет электронное письмо через адаптированный сервис.

        Параметры:
        message : str
            Текст сообщения для отправки.
        recipient : str
            Адрес электронной почты получателя.
        """
        self.email_service.send_email(recipient, message)


class PushAdapter(MessageSender):
    def __init__(self, push_service: PushService):
        """
        Инициализирует адаптер для отправки Push-уведомлений.

        Параметры:
        push_service : PushService
            Экземпляр сервиса для отправки Push-уведомлений.
        """
        self.push_service = push_service

    def send_message(self, message: str, recipient: str) -> None:
        """
        Отправляет Push-уведомление через адаптированный сервис.

        Параметры:
        message : str
            Текст сообщения для отправки.
        recipient : str
            Идентификатор устройства получателя.
        """
        self.push_service.send_push(recipient, message)



class MessageDispatcher:
    def __init__(self, adapters):
        self.adapters = adapters

    def send_all(self, message: str):
        for adapter in self.adapters:
            adapter.send_message(message)


# Пример использования
if __name__ == "__main__":
    # Создание адаптеров для каждого типа сервиса
    sms_adapter = SMSAdapter(SMSService())
    email_adapter = EmailAdapter(EmailService())
    push_adapter = PushAdapter(PushService())

    # Отправка сообщений через адаптеры
    sms_adapter.send_message("это тестовое SMS.", "380634575578")
    email_adapter.send_message("это тестовое Email.", "shop_tech@example.com")
    push_adapter.send_message("это тестовое Push уведомление.", "iphone")
