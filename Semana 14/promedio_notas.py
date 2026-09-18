# Definición de la función con parámetros y retorno de valores
def calcular_promedio(nota1, nota2, nota3):
    """Calcula el promedio de tres notas."""
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio

# --- Flujo principal del programa ---
print("--- SISTEMA PARA CALCULAR EL PROMEDIO DE TRES NOTAS ---")

# Solicitamos las notas al usuario (usamos float por si ingresa decimales)
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))

# Llamada a la función pasando los argumentos y guardando el resultado devuelto (return)
resultado_final = calcular_promedio(n1, n2, n3)

# Mostrar el resultado final en pantalla
print(f"El promedio final de las tres notas es: {resultado_final:.2f}")