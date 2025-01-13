def suma(a,b):
    """
    >>> suma(5, 7)
    12
    """    
    return a + b



def resta(a,b):
    return a-b


def division(a,b):
    """
    >>> division(10, 0)
    Traceback (most recent call last):
    ValueError: La division por cero no esta permitida
    """
    if b==0:
        raise ValueError("La division por cero no esta permitida")

    return a/b

# para poder hechar a correr las pruebas con doctest se utiliza este comando
# python -m doctest src/prueba_doctest.py