def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print("Palabra: " + palabra)
    longitud = str(len(palabra))
    print("Longitud: " + longitud)
    print("Primera letra: " + palabra [0])
    print("Ultima letra: " + palabra[-1])
    print("Repetida: " + palabra * 3)
    print("Decorada: " + "***" + palabra + "***")
string_info()