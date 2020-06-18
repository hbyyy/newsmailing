from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

User = get_user_model()


@shared_task
def send_auth_mail_task(email, message):
    email = EmailMessage('[Newsmail]구독 인증 메일', message, to=[email])
    email.content_subtype = 'html'
    return email.send()
