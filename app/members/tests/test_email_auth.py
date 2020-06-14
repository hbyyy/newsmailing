import pytest
from django.core import mail
from faker import Faker

from config.settings import EMAIL_HOST_USER


@pytest.mark.django_db
def test_email_auth(django_user_model, client):
    faker = Faker()
    user = django_user_model.objects.create_user(email=faker.email())

    assert user.is_active is False

    mail.send_mail('test에서 보낸 메일입니다',
                   'test에서 보낸 메일입니다',
                   EMAIL_HOST_USER,
                   ['qjaduddl94@gmail.com'])

    # 보낸 메일은 mail.outbox로 간다.
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'test에서 보낸 메일입니다'
    assert mail.outbox[0].body == 'test에서 보낸 메일입니다'
    assert mail.outbox[0].from_email == EMAIL_HOST_USER
    assert mail.outbox[0].to == ['qjaduddl94@gmail.com']

