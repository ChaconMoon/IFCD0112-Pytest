# Empieza a testear tus proyectos de Python con Pytest

![](images/Pytest_logo.svg)

Pytest es un framework de testing para python similar a unittest pero con algunas mejoras, entre ellas:
- detección automatica de tests, encontrará automaticamente los tests de nuestro proyecto.
- Permite ejecutarse facilmente desde la terminal simplmente con el comando `pytest`
- Tiene una sintaxis bastante sencilla.
- Permite elegir como de completos queremos que sean los logs de los errores.

## Instalación se instala como cualquier paquete de Python usando pip.

```bash
pip install pytest
```
Esto nos instalara pytest en la terminal y como un paquete de python.

## Crear nuestro primer tests.

### Aserciones

Creamos un nuevo proyecto en Python, si no lo tenemos creado ya y en la raiz del proyecto, donde esta el .gitignore, el .env..., creamos una carpeta que se llame `tests`, tiene que llamarse asi para que pytest la reconozca y dentro de ella creamos un modulo que se llame `test_operaciones.py`
> [!WARNING]
> TODOS los modulos que sean tests y todos los tests deben empezar por `test_` para que pytest los reconozca

Dentro de ese modulo importamos pytest y creamos una función llamada `test_suma_tres_cinco`

```python
def test_suma_tres_cinco():
    resultado = 3 + 5
```

De momento esto es una funcion normal, simplemente suma 2 números que dan como resultado 8. pero... ¿Sabemos si el resultado es 8? Es decir es matematica muy basica, pero en la programación nada es seguro hasta que se prueba, justo debajo añadimos una linea que diga `asset resultado == 8`

```python
def test_suma_tres_cinco():
    resultado = 3 + 5
    assert resultado == 8
```

Si ahora ejecutamos en la terminal:

``` bash
pytest
```

Si los test son correctos veremos algo asi. Lo que nos importa es la ultima linea '1 passed' es decir nuestro programa ha pasado el test
```
==================================================== test session starts ====================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\Clases_Carlos\IFCD0112-Pytest
configfile: pyproject.toml
collected 1 item                                                                                                            

tests\test_operaciones.py .                                                                                            [100%]

===================================================== 1 passed in 0.04s =====================================================
```

Si en lugar de `pytest` usamos esto le estamos diciendo que queremos un resultado mas "verbose" si no te suena esta palabra es ser mas detallado:

```
pytest -v
```
Aqui vemos explicitamente que test se estan ejecutando y si pasan o no, si algún test concreto falla podemos verlo facilmente aqui.
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
> Si solo deseamos ejecutar un modulo en concreto podemos pasarle la ruta del modulo como parametro dentro de la función a pytest. `pytest .\tests\test_operaciones.py`
> 
> Si además queremos ejecutar un  unico test de un modulo concreto se lo podemos indicar con la misma forma que nos lo muestra al devolverlo `tests/test_operaciones.py::test_suma_tres_cinco`

### Excepciones

No solo podemos controlar que se ha devuelto un valor correcto, tambien podemos comprobar que se ha lanzado una excepción determinada, esto nos permitira saber si el programa falla o si esta lanzando la excepción correcta, dentro del mismo fichero de tests crea el siguiente test:

```python
def test_dividir_diez_cero():
    with pytest.raises(ZeroDivisionError):
        resultado = 10 / 0
```

Python tiene una excepción que salta cuando intentas dividir por 0, este test comprueba que efectivamente salta esa excepción, pruebalo con:

```bash
pytest tests/test_operaciones.py::test_dividir_diez_cero -v
```
