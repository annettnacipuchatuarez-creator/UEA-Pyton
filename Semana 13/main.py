# Definición de la función con dos parámetros
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

# Bloque principal del programa
if __name__ == "__main__":
    # Damos valores de ejemplo
    precio_producto = 10.0
    cantidad_producto = 3

    # Llamamos a la función y guardamos el resultado
    resultado = calcular_total(precio_producto, cantidad_producto)

    # Mostramos el resultado en la consola
    print("El precio del producto es:", precio_producto)
    print("La cantidad llevada es:", cantidad_producto)
    print("El total a pagar es:", resultado)
    