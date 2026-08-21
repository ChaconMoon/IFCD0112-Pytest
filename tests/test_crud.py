from unittest.mock import MagicMock, patch
from connector import UserCRUDSQLite # Importar la clase UserCRUDSQLite desde el módulo connector
 
def test_create_user_with_mocker(): # Definición de un test que utiliza mocker para simular la creación de un usuario

    # --------------------------------------- Preparación ---------------------------------------
    crud = UserCRUDSQLite(":memory:") # Usar una base de datos en memoria para pruebas
    mock_cursor = MagicMock() # Usar un mock para el cursor
    mock_cursor.lastrowid = 1 # Establecemos la linea del último usuario creado, en este caso el primero

    mock_conn = MagicMock() # Usamos un mock para el cursor
    mock_conn.__enter__.return_value = mock_conn 
    mock_conn.execute.return_value = mock_cursor # Cuando la comexión ejecute el metodo execute devolvera el cursor.

    # --------------------------------------- Preparación ---------------------------------------

    # ----------------------------------------- Acción ------------------------------------------
    
    # Parcheamos la función '_connect' de nuestro crud para que en lugar de devolvernos una conexión real devuelve una conexión mockeada.
    with patch.object(crud, '_connect', return_value=mock_conn):
        user_id = crud.create_user("usuario123", "alumno@correo.com", "Clave123!")

    # ----------------------------------------- Acción ------------------------------------------

    # -------------------------------------- Verificación ---------------------------------------

    # En el cursor le hemos indicado que la ultima fila es la 1.
    # Si al crear el usuario el ID que tiene es 1 es que la función create user devuelve el valor correcto.
    assert user_id == 1

    # Estamos comprobando que el metodo commit de la conexión se ha ejecutado
    mock_conn.commit.assert_called_once()

    # Estamos comprobando que la función execute se ejecuta una vez.
    mock_conn.execute.assert_called_once()

    # -------------------------------------- Verificación ---------------------------------------


def test_update_user_with_mocker():
    # --------------------------------------- Preparación ---------------------------------------
    crud = UserCRUDSQLite(":memory:") # Usar una base de datos en memoria para pruebas
    mock_cursor = MagicMock() # Usar un mock para el cursor
    mock_cursor.rowcount = 1 # Establecemos la linea del último usuario creado, en este caso el primero

    mock_conn = MagicMock() # Usamos un mock para el cursor
    mock_conn.__enter__.return_value = mock_conn 
    mock_conn.execute.return_value = mock_cursor # Cuando la comexión ejecute el metodo execute devolvera el cursor.
    # --------------------------------------- Preparación ---------------------------------------

    # ----------------------------------------- Acción ------------------------------------------

    with patch.object(crud, '_connect', return_value=mock_conn):
        user_id = crud.update_user( 1, "usuario123", "alumno@correo.com", "Clave123!")
    
        # En el cursor le hemos indicado que la ultima fila es la 1.
        # Si al crear el usuario el ID que tiene es 1 es que la función create user devuelve el valor correcto.
        assert user_id == 1

    # ----------------------------------------- Acción ------------------------------------------

    # -------------------------------------- Verificación ---------------------------------------
    
        # Estamos comprobando que el metodo commit de la conexión se ha ejecutado
        mock_conn.commit.assert_called_once()
    
        # Estamos comprobando que la función execute se ejecuta una vez.
        mock_conn.execute.assert_called_once()

    # -------------------------------------- Verificación ---------------------------------------