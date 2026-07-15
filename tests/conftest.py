import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test.utils import setup_databases, teardown_databases
from ninja.testing import TestClient
from testcontainers.postgres import PostgresContainer

from attributes.models import Attribute
from authentication.auth import create_jwt_token
from category.models import Category, Family
from core.api import api
from product_type.models import ProductType

User = get_user_model()


@pytest.fixture(scope='session')
def postgres_container():
    with PostgresContainer('postgres:17', driver='psycopg') as postgres:
        yield postgres


@pytest.fixture(scope='session')
def django_db_setup(postgres_container, django_db_blocker):
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': postgres_container.dbname,
        'USER': postgres_container.username,
        'PASSWORD': postgres_container.password,
        'HOST': postgres_container.get_container_host_ip(),
        'PORT': postgres_container.get_exposed_port(5432),
    }

    with django_db_blocker.unblock():
        db_cfg = setup_databases(verbosity=1, interactive=False)

    yield

    with django_db_blocker.unblock():
        teardown_databases(db_cfg, verbosity=1)


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


@pytest.fixture
def attribute(db):
    attribute = Attribute.objects.create(
        name='Cor',
        expected_value='Amarelo',
        is_active='True',
    )

    return attribute
