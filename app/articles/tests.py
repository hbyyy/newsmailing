import pytest


# Create your tests here.


@pytest.mark.django_db
class TestArticlesModel:
    pytestmark = pytest.mark.django_db

    def test_article(self):
        pass
