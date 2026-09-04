# Tarea Semana 12: Reserva de un asiento en sala de cine

def mostrar_sala(asientos):
    """Función para mostrar el estado actual de la sala en formato de tabla"""
    print("\n--- ESTADO ACTUAL DE LA SALA DE CINE ---")
    print("Leyenda: 0 = Libre, 1 = Reservado\n")
    print("      Col 0  Col 1  Col 2  Col 3")
    print("    +----------------------------+")
    
    # Bucle anidado para recorrer la matriz e imprimirla fila por fila
    for i in range(len(asientos)):
        print(f"Fila {i} |", end=" ")
        for j in range(len(asientos[i])):
            print(f"  {asientos[i][j]}  ", end=" ")
        print("|")
    print("    +----------------------------+\n")

def main():
    # 1. Crear una matriz de 3 filas por 4 columnas llamada 'asientos', inicializada en 0
    # Usamos una lista de listas (comprensión de listas)
    asientos = [[0 for _ in range(4)] for _ in range(3)]
    
    print("¡Bienvenido al sistema de reservas del cine!")
    
    # Mostramos la sala inicial vacía
    mostrar_sala(asientos)
    
    # 2. Pedir al usuario la fila y la columna del asiento que desea reservar
    # Usamos try-except por seguridad para evitar que el programa falle si ingresan letras
    try:
        fila = int(input("Ingrese el número de fila (0 a 2): "))
        columna = int(input("Ingrese el número de columna (0 a 3): "))
        
        # Validar que la fila y la columna estén dentro del rango permitido
        if 0 <= fila <= 2 and 0 <= columna <= 3:
            # Verificar si el asiento ya está reservado
            if asientos[fila][columna] == 1:
                print("\n¡Atención! Este asiento ya se encuentra reservado. Elija otro.")
            else:
                # 3. Marcar ese asiento como reservado asignándole el valor 1
                asientos[fila][columna] = 1
                print(f"\n¡Reserva exitosa para el asiento de la Fila {fila}, Columna {columna}!")
                
                # 4. Mostrar la matriz completa actualizada usando bucles anidados
                mostrar_sala(asientos)
        else:
            print("\nError: La fila debe estar entre 0 y 2, y la columna entre 0 y 3.")
            
    except ValueError:
        print("\nError: Por favor, ingrese únicamente números enteros válidos.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()