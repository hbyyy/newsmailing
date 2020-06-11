import pytest
from faker import Faker


# Create your tests here.


@pytest.mark.django_db
def test_user(django_user_model):
    fake = Faker()

    normal_user = django_user_model.objects.create_user(email=fake.email())
    admin_user = django_user_model.objects.create_superuser(email=fake.email(), password=fake.password())

    assert django_user_model.objects.count() == 2
    assert django_user_model.objects.filter(is_superuser=True).count() == 1
    assert django_user_model.objects.filter(is_superuser=False).count() == 1
    assert normal_user.is_staff is False
    assert admin_user.is_staff is True


@pytest.mark.django_db
def test_expire_user(django_user_model, create_expire_user):
    user = create_expire_user()
    user.save()

    assert django_user_model.objects.expired().count() == 1
