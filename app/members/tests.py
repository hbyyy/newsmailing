from faker import Faker
import pytest

# Create your tests here.
from model_bakery import baker


@pytest.mark.django_db
def test_user(django_user_model):
    fake = Faker()

    normal_user = django_user_model.objects.create_user(email=fake.email())
    admin_user = django_user_model.objects.create_superuser(email=fake.email(), password=fake.password())

    assert django_user_model.objects.count() == 2
    assert django_user_model.objects.filter(is_superuser=True).count() == 1
    assert django_user_model.objects.filter(is_superuser=False).count() == 1

