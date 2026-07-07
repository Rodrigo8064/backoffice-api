def test_create_product_type(client, auth_headers):
    response = client.post(
        '/products/',
        headers=auth_headers,
        json={
            'name': 'Informativa',
            'is_active': 'True',
        },
    )

    assert response.status_code == 201


def test_create_product_type_unauthorize(client):
    response = client.post(
        '/products/',
        json={
            'name': 'Informativa',
            'is_active': 'True',
        },
    )

    assert response.status_code == 401


def test_list_products_type(client, auth_headers):
    response = client.get(
        '/products/',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_list_products_type_with_search(
    client, auth_headers, product_type_father
):
    response = client.get(
        f'/products/?parent={product_type_father.id}',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1
    assert data['items'][0]['name'] == 'Informatica'


def test_list_products_type_with_family(
    client, auth_headers, product_type_father, product_type_children
):

    response = client.get(
        f'/products/?parent={product_type_father.id}',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_list_products_typet_does_not_exists(
    client, auth_headers, product_type_father
):
    response = client.get(
        '/products/?parent=999',
        headers=auth_headers,
    )

    assert response.status_code == 200


def test_get_products_type_by_id(client, auth_headers, product_type_father):
    response = client.get(
        '/products/1',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Informatica'


def test_get_product_type_by_name(client, auth_headers, product_type_father):

    response = client.get(
        '/products/name/Informatica',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Informatica'


def test_get_product_type_by_name_does_not_exists(
    client, auth_headers, product_type_father
):

    response = client.get(
        '/products/name/banana',
        headers=auth_headers,
    )

    assert response.status_code == 404


def test_update_product_type(
    client, auth_headers, product_type_father, product_type_children
):

    response = client.put(
        f'/products/{product_type_children.id}',
        headers=auth_headers,
        json={'name': 'mouse'},
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'mouse'


def test_delete_product_type(
    client, auth_headers, product_type_father, product_type_children
):
    response = client.delete(
        f'/products/{product_type_children.id}',
        headers=auth_headers,
    )

    assert response.status_code == 204
