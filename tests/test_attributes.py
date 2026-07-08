def test_create_attributes(client, auth_headers, family):
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
