import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage


def format_message_html(content, interest):
    name = content["name"]
    email = content["email"]
    phone = content["phone"]
    company = content["company"]
    return f'Имя: {name}<br>email: {email}<br>Телефон: {phone}<br>Компания: {company}<br>Чем интересовались: {interest}'


def format_message_telegram(content, interest):
    name = content["name"]
    email = content["email"]
    phone = content["phone"]
    company = content["company"]
    return f'Новая заявка!\nИмя: {name}\nemail: {email}\nТелефон: {phone}\nКомпания: {company}\n' \
           f'Чем интересовались: {interest}'


@shared_task()
def send_mail(content, interest, recipient_list):
    message_html = format_message_html(content, interest)
    msg = EmailMessage('Новая заявка', message_html, settings.EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html"
    msg.send()


@shared_task()
def send_telegram(content, interest):
    message_telegram = format_message_telegram(content, interest)
    requests.post(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
                  data={'chat_id': '1489427084', 'text': {message_telegram}})
