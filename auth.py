"""Authentication logic shared by the login UI and automated checks."""


def authenticate(username, password):
    """Validate the demo credentials used by the V1 login screen."""
    return username == "admin" and password == "1234"
