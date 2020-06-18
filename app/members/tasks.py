from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

User = get_user_model()


@shared_task
def send_auth_mail(user_id):
    user = User.objects.get(pk=user_id)
    html_message = render_to_string('email/signup_email.html',
                                    context={'user': user})
    email = EmailMessage('[Newsmail]구독 인증 메일', html_message, to=[user.email])
    email.content_subtype = 'html'
    return email.send()
