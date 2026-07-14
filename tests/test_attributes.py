def test_create_attribute(client, auth_headers, family):
    response = client.post(
        path='/attributes/',
        headers=auth_headers,
        json={
            'name': 'Cor',
            'expected_value': 'Amarelo',
            'is_active': 'True',
            'families_id': [family.id],
        },
    )

    assert response.status_code == 201


def test_create_attribute_unauthorize(client, family):
    response = client.post(
        path='/attributes/',
        json={
            'name': 'Cor',
            'expected_value': 'Amarelo',
            'is_active': 'True',
            'families_id': [family.id],
        },
    )

    assert response.status_code == 401


def test_liste_attributes(client, auth_headers):
    response = client.get(
        path='/attributes/',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_get_attribute(client, auth_headers, attribute):
    response = client.get(
        path=f'/attributes/{attribute.id}',
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Cor'


def test_delete_attribute(client, auth_headers, attribute):
    response = client.delete(
        f'/attributes/{attribute.id}',
        headers=auth_headers,
    )

    assert response.status_code == 204


def test_update_attribute(client, auth_headers, attribute, family):
    response = client.put(
        f'/attributes/{attribute.id}',
        headers=auth_headers,
        json={'expected_value': 'Preto', 'families_id': [1]},
    )

    assert response.status_code == 200
    data = response.json()
    assert data['expected_value'] == 'Preto'
    assert data['name'] == 'Cor'


def test_update_attribute_not_found(client, auth_headers):
    response = client.put(
        '/attributes/100',
        headers=auth_headers,
        json={'expected_value': 'Preto'},
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
