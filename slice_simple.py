def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    print(texto[0:3].lower()) #del primer caracter hasta el 3ro (pones uno mas al final porque no lo incluye)
    print(texto[2:5].lower()) #del segundo al cuarto
    print(texto.lower()) #todo el texto en minuscula
#slice_simple()
    