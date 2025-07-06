if token:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    user_url = "https://reqres.in/api/users/2"
    user_response = requests.get(user_url, headers=headers)

    print("User Status:", user_response.status_code)
    print("User Data:", user_response.json())


import requests

def test_get_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    
    assert response.status_code == 200

    json_data = response.json()
    assert json_data["data"]["id"] == 2
    assert json_data["data"]["first_name"] == "Janet"
    assert json_data["data"]["last_name"] == "Weaver"
