# Limpiar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Funcion cuadratica
def Cuadratica(a, b, c):
    # x1
    x1 = (-b + (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
    # x2
    x2 = (-b - (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)

    # Imprimir las soluciones
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

# Programa
print("ENCONTRAR LAS SOLUCIONES DE UNA ECUACION CUADRATICA")
print("aX^2 + bX + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# Invocamos funcion cuadratica
Cuadratica(a, b, c)