from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SignupForm(forms.Form):
    email = forms.EmailField(help_text='이메일을 입력하세요')

    def clean_email(self):
        user_check = User.objects.filter(email=self.cleaned_data['email']).exists()
        if user_check:
            raise ValidationError(_('this email is already subscribed'))
        return self.cleaned_data['email']

    def save(self):
        return User.objects.create_user(email=self.cleaned_data['email'])
