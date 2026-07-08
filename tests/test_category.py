def test_create_category(client, auth_headers):
    response = client.post(
        '/categories/',
        headers=auth_headers,
        json={
            'name': 'Informatica',
            'url': 'IN',
            'is_active': 'True',
            'notes': 'Criada',
        },
    )

    assert response.status_code == 201


def test_create_category_type_unauthorize(client):
    response = client.post(
        '/categories/',
        json={
            'name': 'Informatica',
            'is_active': 'True',
        },
    )

    assert response.status_code == 401


def test_list_categories_type(client, auth_headers):
    response = client.get(
        '/categories/',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_list_categories_type_with_search(
    client, auth_headers, category_father
):
    response = client.get(
        f'/categories/?parent={category_father.id}',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1
    assert data['items'][0]['name'] == 'Informatica'


def test_list_categories_type_with_family(
    client, auth_headers, category_father, category_children
):

    response = client.get(
        f'/categories/?parent={category_father.id}',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_list_categories_typet_does_not_exists(
    client, auth_headers, category_father
):
    response = client.get(
        '/categories/?parent=999',
        headers=auth_headers,
    )

    assert response.status_code == 200


def test_get_categories_by_id(client, auth_headers, category_father):
    response = client.get(
        '/categories/1',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Informatica'


def test_get_category_by_name(client, auth_headers, category_father):

    response = client.get(
        '/categories/name/Informatica',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Informatica'


def test_get_category_by_name_does_not_exists(
    client, auth_headers, category_father
):

    response = client.get(
        '/categories/name/banana',
        headers=auth_headers,
    )

    assert response.status_code == 404


def test_update_category(
    client, auth_headers, category_father, category_children
):

    response = client.put(
        f'/categories/{category_children.id}',
        headers=auth_headers,
        json={'name': 'mouse'},
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'mouse'


def test_delete_category_type(
    client, auth_headers, category_father, category_children
):
    response = client.delete(
        f'/categories/{category_children.id}',
        headers=auth_headers,
    )

    assert response.status_code == 204
