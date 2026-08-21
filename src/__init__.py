from models import User
from connector import UserCRUDSQLite

def main():
        # Crear una instancia de UserCRUDSQLite
        user_crud = UserCRUDSQLite("users.db")
        
        # Inicializar la base de datos
        user_crud.init_db()

        user_id = 0  # Inicializar user_id para usarlo más adelante

        # Crear un nuevo usuario
        try:
                user_id = user_crud.create_user(
                username="usuario123",
                email="usuario123@example.com",
                password="Clave123!"
                )
                print(f"Usuario creado con ID: {user_id}")

        except ValueError as e:
                print(f"Error al crear usuario: {e}")

        try:
                # Obtener un usuario por ID
                user = user_crud.get_user_by_id(user_id)
                if user:
                    print(f"Usuario obtenido: {user}")
                else:
                    print("Usuario no encontrado")
        except Exception as e:
                print(f"Error al obtener usuario: {e}")

        try:
               user_crud.update_user(
                      user_id, username="nuevo_usuario", 
                      email="nuevo_usuario@example.com", 
                      password="NuevaClave123!"
                )
        except Exception as e:
                print(f"Error al actualizar usuario: {e}")

if __name__ == "__main__":

    main()