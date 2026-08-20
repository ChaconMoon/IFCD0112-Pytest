import pytest

from models import User


def test_user_accepts_valid_data():
    user = User("usuario01", "usuario@example.com", "Clave123!")

    assert user.username == "usuario01"
    assert user.email == "usuario@example.com"
    assert user.password == "Clave123!"


@pytest.mark.parametrize("username", ["corto", "a" * 17])
def test_user_rejects_username_outside_length_limits(username):
    with pytest.raises(ValueError, match="entre 8 y 16"):
        User(username, "usuario@example.com", "Clave123!")


@pytest.mark.parametrize("email", ["usuario", "usuario@example", "@example.com"])
def test_user_rejects_invalid_email(email):
    with pytest.raises(ValueError, match="email"):
        User("usuario01", email, "Clave123!")


@pytest.mark.parametrize("password",["clave123!", "CLAVE123!", "Claveabc!", "Clave123"],
)
def test_user_rejects_password_without_required_character_type(password):
    with pytest.raises(ValueError, match="contraseña"):
        User("usuario01", "usuario@example.com", password)

def test_user_printable_representation():
    user = User("usuario01", "usuario@example.com", "Clave123!")
    assert repr(user) == f"Usuario: {user.username}\nEmail: {user.email}\nContraseña: {user.password}"

def test_change_username_accepts_valid_username():
    user = User("usuario01", "usuario@example.com", "Clave123!")
    user.change_username("nuevoUsuario")
    assert user.username == "nuevoUsuario"

@pytest.mark.parametrize("new_username", ["corto", "a" * 17])
def test_change_username_rejects_invalid_username(new_username):
    user = User("usuario01", "usuario@example.com", "Clave123!")
    with pytest.raises(ValueError, match="entre 8 y 16"):
        user.change_username(new_username)