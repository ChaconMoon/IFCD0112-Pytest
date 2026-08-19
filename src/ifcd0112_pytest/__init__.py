from ifcd0112_pytest.models import User

def main():
        user = User("usuario01", "usuario@example.com", "Clave123!")
        print(user)

if __name__ == "__main__":

    main()