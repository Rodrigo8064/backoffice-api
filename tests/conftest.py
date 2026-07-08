import pytest
from django.contrib.auth import get_user_model
from ninja.testing import TestClient

from authentication.auth import create_jwt_token
from category.models import Category, Family
from core.api import api
from product_type.models import ProductType

User = get_user_model()


@pytest.fixture
def client():
    return TestClient(api)


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        username='test_driver',
        email='test@example.com',
        password='123deoliveira4',
    )
    return user


@pytest.fixture
def auth_headers(user):
    token = create_jwt_token(user.id)
    return {'Authorization': f'Bearer {token}'}


@pytest.fixture
def product_type_father(db):
    product_type = ProductType.objects.create(
        name='Informatica',
        is_active='True',
    )

    return product_type


@pytest.fixture
def product_type_children(db):
    product_type = ProductType.objects.create(
        name='Teclado',
        is_active='True',
        parent_id=1,
    )

    return product_type


@pytest.fixture
def category_father(db):
    category = Category.objects.create(
        name='Informatica',
        url='IN',
        is_active='True',
    )

    return category


@pytest.fixture
def category_children(db):
    category = Category.objects.create(
        name='Teclado',
        url='TECL',
        is_active='True',
        parent_id=1,
        notes='Criada',
    )

    return category


@pytest.fixture
def family(db):
    family = Family.objects.create(
        name='Esporte e Lazer',
        is_active='True',
    )

    return family
