def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input("Cantidad: "))
    print("Precio:", precio)
    print("Descuento:", descuento)
    precio_descuento = precio - descuento
    print("Precio con descuento:", precio_descuento)
    total = precio_descuento * cantidad
    print("Total:", total)
casting()
    