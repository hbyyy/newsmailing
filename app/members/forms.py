from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SignupForm(forms.Form):
    email = forms.EmailField(help_text='이메일을 입력하세요')

    def clean_email(self):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        else:
            if user.is_active is True:
                raise ValidationError(_('this email is already subscribed'))
            else:
                raise ValidationError(_('check your email, and activate'))

    def save(self):
        return User.objects.create_user(email=self.cleaned_data['email'])

    def send_mail(self, user):
        html_message = render_to_string('email/signup_email.html',
                                        context={'user': user})
        email = EmailMessage('[Newsmail]구독 인증 메일', html_message, to=[user.email])
        email.content_subtype = 'html'
        return email.send()
