# Introducción al Testing en Python con Pytest

![](images/Pytest_logo.svg)

Pytest es un framework de testing para Python similar a `unittest` pero con importantes ventajas:
- **Detección automática de tests:** Encuentra automáticamente los archivos y funciones de prueba de nuestro proyecto.
- **Ejecución sencilla:** Se ejecuta fácilmente desde la terminal simplemente con el comando `pytest`.
- **Sintaxis limpia:** Tiene una sintaxis bastante sencilla basada en `assert`.
- **Logs configurables:** Permite elegir cómo de detallados queremos que sean los reportes de error.

---

## 📋 Tabla de Contenidos

1. [Instalación](#instalación)
2. [Crear nuestro primer test](#crear-nuestro-primer-test)
   - [Aserciones](#aserciones)
   - [Excepciones](#excepciones)
3. [Pruebas en un software real](#pruebas-en-un-software-real)
4. [Mockear](#mockear)
   - [Fase 1: Preparación](#fase-1-preparación)
   - [Fase 2: Acción](#fase-2-acción)
   - [Fase 3: Verificación](#fase-3-verificación)
5. [Casos de uso](#casos-de-uso)
6. [Tipos de pruebas](#tipos-de-pruebas)

---

## Instalación

Se instala como cualquier paquete de Python usando pip:

```bash
pip install pytest
```

Esto nos instalará `pytest` en la terminal y como paquete de Python.

---

## Crear nuestro primer test

### Aserciones

Creamos un nuevo proyecto en Python (si no lo tenemos creado ya). En la raíz del proyecto, donde están `.gitignore`, `.env`, etc., creamos una carpeta llamada `tests`. Dentro de ella creamos un módulo llamado `test_operaciones.py`.

> [!WARNING]
> TODOS los módulos que sean tests y todas las funciones de test deben empezar por `test_` para que Pytest los reconozca automáticamente.

Dentro de ese módulo creamos una función llamada `test_suma_tres_cinco`:

```python
def test_suma_tres_cinco():
    resultado = 3 + 5
```

De momento esto es una función normal: simplemente suma 2 números que dan como resultado 8. Pero... ¿cómo sabemos si el resultado es 8? En la programación nada es seguro hasta que se prueba, asi que justo debajo añadimos una línea con `assert` para comprobar que el resultado es el esperado:

```python
def test_suma_tres_cinco():
    resultado = 3 + 5
    assert resultado == 8
```

Ahora ejecutamos en la terminal:

```bash
pytest
```

En caso de que los tests son correctos veremos algo así. La última línea (`1 passed`) nos indica que nuestro programa ha superado la prueba:

```
==================================================== test session starts ====================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\Clases_Carlos\IFCD0112-Pytest
configfile: pyproject.toml
collected 1 item                                                                                                            

tests\test_operaciones.py .                                                                                            [100%]

===================================================== 1 passed in 0.04s =====================================================
```

Podemos usar la flag `-v` (*verbose*), para indicar que queremos un resultado más detallado:

```
pytest -v
```

Aquí vemos explícitamente qué tests se están ejecutando y si pasan o no:

```
==================================================== test session starts ====================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0 -- D:\Clases_Carlos\IFCD0112-Pytest\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\Clases_Carlos\IFCD0112-Pytest
configfile: pyproject.toml
collected 1 item                                                                                                             

tests/test_operaciones.py::test_suma_tres_cinco PASSED                                                                 [100%]

===================================================== 1 passed in 0.06s =====================================================
```

> [!NOTE]
> - Si solo deseamos ejecutar un módulo en concreto, podemos pasarle la ruta: `pytest .\tests\test_operaciones.py`
> - Si además queremos ejecutar un único test de un módulo concreto, se lo indicamos con la sintaxis: `pytest tests/test_operaciones.py::test_suma_tres_cinco`

### Excepciones

No solo podemos comprobar que se ha devuelto un valor correcto; también podemos verificar que se lanza una excepción determinada ante situaciones erróneas.

Dentro del mismo fichero de tests añade:

```python
def test_dividir_diez_cero():
    with pytest.raises(ZeroDivisionError):
        resultado = 10 / 0
```

Python tiene una excepción que salta cuando intentas dividir por 0 (`ZeroDivisionError`). Este test comprueba que efectivamente salta dicha excepción. Puedes probarlo con:

```bash
pytest tests/test_operaciones.py::test_dividir_diez_cero -v
```

---

## Pruebas en un software real

Vamos a crear un pequeño software que vamos a testear: un gestor de usuarios. En la raíz del proyecto creamos una carpeta llamada `src` y dentro un módulo llamado `models.py`.

Los requisitos de nuestro sistema son los siguientes:
- El nombre del usuario debe tener entre 8 y 16 caracteres.
- El correo debe cumplir con un formato válido de dirección de correo.
- La contraseña debe contener al menos una minúscula, una mayúscula, un número y un carácter no alfanumérico.

```python
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
```

Dentro de `tests` creamos otro módulo llamado `test_models.py` para probar los campos uno a uno:

### 1. Comprobación de datos válidos
```python

import pytest

from ifcd0112_pytest.models import User


def test_user_accepts_valid_data():
    user = User("usuario01", "usuario@example.com", "Clave123!")

    assert user.username == "usuario01"
    assert user.email == "usuario@example.com"
    assert user.password == "Clave123!"

```

### 2. Comprobación de longitud de usuario con `@pytest.mark.parametrize`
Con `@pytest.mark.parametrize` podemos pasar una lista de parámetros para ejecutar el test por cada uno de ellos. En este caso probamos dos nombres: uno demasiado corto y otro demasiado largo.

```python
@pytest.mark.parametrize("username", ["corto", "a" * 17])
def test_user_rejects_username_outside_length_limits(username):
    with pytest.raises(ValueError, match="entre 8 y 16"):
        User(username, "usuario@example.com", "Clave123!")
```

### 3. Comprobación de formato de email
Comprobamos que el correo electrónico debe tener una estructura completa y válida:

```python
@pytest.mark.parametrize("email", ["usuario", "usuario@example", "@example.com"])
def test_user_rejects_invalid_email(email):
    with pytest.raises(ValueError, match="email"):
        User("usuario01", email, "Clave123!")

```

### 4. Comprobación de requisitos de contraseña
Comprobamos los casos en los que la contraseña no cumple todos los requerimientos de seguridad:

```python
@pytest.mark.parametrize("password",["clave123!", "CLAVE123!", "Claveabc!", "Clave123"],
)
def test_user_rejects_password_without_required_character_type(password):
    with pytest.raises(ValueError, match="contraseña"):
        User("usuario01", "usuario@example.com", password)
```

### 5. Representación en cadena (`__repr__`)
Testeamos que la representación devuelta coincide exactamente con el formato esperado:

```python
def test_user_printable_representation():
    user = User("usuario01", "usuario@example.com", "Clave123!")
    assert repr(user) == f"Usuario: {user.username}\nEmail: {user.email}\nContraseña: {user.password}"
```

### 6. Métodos del objeto
Probamos que al ejecutar el método de cambiar nombre, este se actualiza correctamente:

```python
def test_change_username_accepts_valid_username():
    user = User("usuario01", "usuario@example.com", "Clave123!")
    user.change_username("nuevoUsuario")
    assert user.username == "nuevoUsuario"
```

Por último, comprobamos que no se permita cambiar a un nombre inválido:

```python
@pytest.mark.parametrize("new_username", ["corto", "a" * 17])
def test_change_username_rejects_invalid_username(new_username):
    user = User("usuario01", "usuario@example.com", "Clave123!")
    with pytest.raises(ValueError, match="entre 8 y 16"):
        user.change_username(new_username)
```

---

## Mockear

Los tests unitarios deben caracterizarse por ser **independientes entre sí e independientes del sistema** (incluyendo el sistema de archivos, la red o bases de datos externas). Por ejemplo, si tenemos una base de datos y queremos testear que se formatea bien la información, no pretendemos depender de una base de datos real durante la prueba.

Para lograr este aislamiento realizamos lo que se conoce como **mockear**: simular o imitar la respuesta de un componente interno o dependencia externa.

![Crud vs Tests](<images/Crud vs Tests.png>)

En un flujo normal:
1. Iniciamos la base de datos.
2. Creamos una conexión.
3. Con esa conexión creamos un cursor para navegar y operar.
4. En base a ese cursor obtenemos registros o IDs.

Para verificar nuestro código sin depender del entorno externo, dividimos el test en 3 fases: **Preparación**, **Acción** y **Verificación** (**Arrange**, **Act**, **Assert**).

Crea un módulo llamado `test_crud.py` con las siguientes importaciones:

```python
from unittest.mock import MagicMock, patch
from connector import UserCRUDSQLite # Importar la clase UserCRUDSQLite desde el módulo connector
```

### Fase 1: Preparación 

Preparamos los objetos que vamos a usar para la prueba. Definimos los mocks desde el que no depende de nada hasta el que más depende (el cursor depende de la conexión, por lo que empezamos por el cursor):

```py
    # --------------------------------------- Preparación ---------------------------------------

    crud = UserCRUDSQLite(":memory:") # Usar una base de datos en memoria para pruebas
    mock_cursor = MagicMock() # Usar un mock para el cursor
    mock_cursor.lastrowid = 1 # Establecemos la linea del último usuario creado, en este caso el primero

    mock_conn = MagicMock() # Usamos un mock para el cursor
    mock_conn.__enter__.return_value = mock_conn 
    mock_conn.execute.return_value = mock_cursor # Cuando la comexión ejecute el metodo execute devolvera el cursor.

    # --------------------------------------- Preparación ---------------------------------------
```

### Fase 2: Acción

Ejecutamos la función a testear parcheando el método `_connect` para que use nuestra conexión simulada en lugar de una real:

```py
    with patch.object(crud, '_connect', return_value=mock_conn):
        user_id = crud.create_user("usuario123", "alumno@correo.com", "Clave123!")
```

### Fase 3: Verificación

Comprobamos que los resultados recibidos coinciden con lo esperado:
- Que el ID de usuario devuelto sea `1`.
- Que la función `execute` se ejecutó una vez.
- Que la función `commit` se ejecutó una vez.

```py
    # En el cursor le hemos indicado que la ultima fila es la 1.
    # Si al crear el usuario el ID que tiene es 1 es que la función create user devuelve el valor correcto.
    assert user_id == 1

    # Estamos comprobando que el metodo commit de la conexión se ha ejecutado
    mock_conn.commit.assert_called_once()

    # Estamos comprobando que la función execute se ejecuta una vez.
    mock_conn.execute.assert_called_once()
```

---

## Casos de uso

Al diseñar los tests de un programa, en un desarrollo completo cada función debería estar testeada en todas sus posibilidades y casos de error. Cada una de esas situaciones representa un **caso de uso**.

Imagina una primera versión de una función:

```py
def suma(numero1, numero2):
        return int(numero1)+int(numero2)
```

Si ampliamos el control de errores:

```py
def suma(numero1, numero2):
    try: 
        return int(numero1)+int(numero2)
    except ValueError:
        raise ValueError("Uno de los valores no es convertible a entero")
    except TypeError:
        raise TypeError("Uno de los 2 valores no es un número")
    except OverflowError:
        raise OverflowError("Fuga de memoria: Uno de los 2 valores es demasiado grande.")
```

Ahora tenemos 4 casos de uso a testear (uno de éxito y tres de control de error):

### Primer caso de uso: Suma correcta
```py
def test_suma_correct(): # Happy Path
    assert suma(3, 5) == 8
```

### Segundo caso de uso: Valor no convertible a int
```py
def test_suma_value_error():
    with pytest.raises(ValueError):
        suma("NaN", 5)
```

### Tercer caso de uso: Tipo no válido
```py
def test_suma_type_error():
    with pytest.raises(TypeError):
        suma(None, 5)
```

### Cuarto caso de uso: Desbordamiento / Valor excesivo
```py
def test_suma_overflow_error():
    with pytest.raises(OverflowError):
        suma(float('inf'), 5)
```

---

## Tipos de pruebas

- **Tests unitarios:** Prueban una parte muy concreta del código en aislamiento (generalmente una función o clase).
- **Tests de integración:** Verifican que varios módulos o funciones cooperan correctamente entre sí.
- **Tests con dependencias externas:** Verifican la comunicación con dependencias externas como APIs o servicios remotos.

Ejemplo con una API externa:

> [!NOTE]
> La librería requests hay que instalarla ya que no viene incluida con python.

```bash
pip install requests
```

```py
import requests

def test_rick_and_morty_api():
    url = "https://rickandmortyapi.com/api/"
    response = requests.get(url)
    
    assert response.status_code == 200
```

> [!NOTE]
> Frameworks como Django tienen su propio soporte para testing con sintaxis y utilidades similares. Puedes consultar la documentación [aquí](https://docs.djangoproject.com/es/stable/topics/testing/overview/).
