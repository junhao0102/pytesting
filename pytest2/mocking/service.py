import requests


database = {1: "Alice", 2: "Bob", 3: "Tom"}


def get_user_from_id(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
