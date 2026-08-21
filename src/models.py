import re # importamos la librería re para poder usar expresiones regulares


class User: # creamos la clase User para representar a un usuario
    def __init__(self, username: str, email: str, password: str): # definimos el método __init__ que se ejecuta al crear un objeto de la clase User
        if not 8 <= len(username) <= 16:
            raise ValueError("El usuario debe tener entre 8 y 16 caracteres") # validamos que el nombre de usuario tenga entre 8 y 16 caracteres, si no es así, lanzamos un ValueError con un mensaje de error

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email): # validamos que el correo electrónico tenga un formato válido usando una expresión regular, si no es así, lanzamos un ValueError con un mensaje de error
            raise ValueError("El email no es válido")

        if ( # validamos que la contraseña cumpla con los requisitos de seguridad, si no es así, lanzamos un ValueError con un mensaje de error
            not any(character.isupper() for character in password)
            or not any(character.islower() for character in password)
            or not any(character.isdigit() for character in password)
            or not any(not character.isalnum() for character in password)
        ): 
            raise ValueError( # lanzamos un ValueError con un mensaje de error si la contraseña no cumple con los requisitos de seguridad
                "La contraseña debe contener mayúsculas, minúsculas, "
                "números y caracteres especiales"
            )

        # Si todas las validaciones pasan, asignamos los valores de los parámetros a los atributos del objeto User
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self): # definimos el método __repr__ que devuelve una representación en cadena del objeto User
        return f"Usuario: {self.username}\nEmail: {self.email}\nContraseña: {self.password}"

    def change_username(self, new_username: str): # definimos el método change_username que permite cambiar el nombre de usuario
        if not 8 <= len(new_username) <= 16: # validamos que el nuevo nombre de usuario tenga entre 8 y 16 caracteres, si no es así, lanzamos un ValueError con un mensaje de error
            raise ValueError("El usuario debe tener entre 8 y 16 caracteres")
        self.username = new_username # si la validación pasa, asignamos el nuevo nombre de usuario al atributo username del objeto User
        
