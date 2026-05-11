users = {

    "admin": "admin123"
}

def authenticate(username, password):

    return users.get(username) == password