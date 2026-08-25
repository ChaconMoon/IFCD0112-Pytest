def suma(numero1, numero2):
    try: 
        return int(numero1)+int(numero2)
    except ValueError:
        raise ValueError("Uno de los valores no es convertible a entero")
    except TypeError:
        raise TypeError("Uno de los 2 valores no es un número")
    except OverflowError:
        raise OverflowError("Fuga de memoria: Uno de los 2 valores es demasiado grande.")