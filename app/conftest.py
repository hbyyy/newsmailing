from datetime import timedelta

import pytest
from model_bakery import baker


@pytest.fixture()
def create_expire_user():
    def make_user(**kwargs):
        user = baker.make('members.User')
        user.created -= timedelta(days=4)
        return user
    return make_user
