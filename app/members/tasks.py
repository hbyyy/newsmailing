from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_auth_mail_task(email, message):
    email = EmailMessage('[Newsmail]구독 인증 메일', message, to=[email])
    email.content_subtype = 'html'
    return email.send()
