import pytest
from django.core import mail
from faker import Faker

from config.settings import EMAIL_HOST_USER


@pytest.mark.django_db
def test_email_auth(django_user_model, client):
    faker = Faker()
    # 테스트를 위한 유저 생성
    user = django_user_model.objects.create_user(email=faker.email())

    assert user.is_active is False

    # 인증메일 보내는 기능 테스트
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

    # 메일 인증 과정 -> user의 is_active가 True로 설정되어야 함

    client.get(user.get_absolute_url())

    user = django_user_model.objects.latest('pk')
    assert user.is_active is True
