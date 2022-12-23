import threading

import requests
from django.conf import settings
from django.core.mail import EmailMessage


class NotificationsThread(threading.Thread):
    def __init__(self, content, interest, recipient_list):
        threading.Thread.__init__(self)
        self.recipient_list = recipient_list
        self.name = content["name"]
        self.email = content["email"]
        self.phone = content["phone"]
        self.company = content["company"]
        self.interest = interest

    def _format_message_html(self):
        return f'Имя: {self.name}<br>email: {self.email}<br>Телефон: {self.phone}<br>' \
               f'Компания: {self.company}<br>Чем интересовались: {self.interest}'

    def _format_message_telegram(self):
        return f'Новая заявка!\nИмя: {self.name}\nemail: {self.email}\nТелефон: {self.phone}\n' \
               f'Компания: {self.company}\nЧем интересовались: {self.interest}'


class EmailThread(NotificationsThread):
    def __init__(self, content, interest, recipient_list):
        super(EmailThread, self).__init__(content, interest, recipient_list)

    def run(self):
        message_html = self._format_message_html()
        msg = EmailMessage('Новая заявка', message_html, settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()


class TelegramThread(NotificationsThread):
    def __init__(self, content, interest, recipient_list):
        super(TelegramThread, self).__init__(content, interest, recipient_list)

    def run(self):
        message_telegram = self._format_message_telegram()
        requests.post(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
                      data={'chat_id': '1489427084', 'text': {message_telegram}})


def send_notifications(content, interest, recipient_list):
    EmailThread(content, interest, recipient_list).start()
    TelegramThread(content, interest, recipient_list).start()



