# 1. Creamos una matriz de 5x5 llena de ceros temporalmente
matriz = [[0 for _ in range(5)] for _ in range(5)]

# 2. Bucle para pedir los valores y guardarlos
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

print("\nMatriz ingresada:")

# 3. Bucle para mostrar la matriz en forma de tabla
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print() # Salto de línea al terminar cada fila