def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    nombre_strip = nombre.strip()
    
    titulo = "FICHA DEL ALUMNO"
    deco = "=" * 24
    print(deco)
    print(titulo.center(24).rstrip())
    print(deco)
    
    print("Nombre:", nombre_strip.title())
    
    print("Email:", email.lower())
    
    print("Caracteres en nombre:", len(nombre_strip))
    
    espacio = nombre_strip.find(" ")
    iniciales = nombre_strip[0].upper() + nombre_strip[espacio + 1].upper()
    print("Iniciales:", iniciales)
    print("Usuario:", nombre_strip[espacio + 1:].lower() + "." + nombre_strip[:espacio].lower())
    
    print("Email valido:", "@" in email)
    arroba = email.find("@")
    print("Dominio:", email[arroba+1 : ].lower())
    
    print("Nombre para archivo:", nombre_strip.replace(" " , "_").title())
    
    print("Cantidad de a:", nombre_strip.lower().count("a"))
    
    print("Codigo secreto:", nombre_strip[::-1].upper())
    
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Nota 3:", nota3)
    suma = nota1 + nota2 + nota3
    print("Suma:", suma)
    promedio = (nota1 + nota2 + nota3) / 3
    print("Promedio:", promedio)
    print("Promedio entero:", round(promedio))
    print(deco)

ficha()