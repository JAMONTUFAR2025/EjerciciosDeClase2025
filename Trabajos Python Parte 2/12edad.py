# Calcular la edad de una persona en Python
# Funciones
def Edad(anioNac, anioAct = 2025):
    edad = anioAct - anioNac
    print(f"Tienes {edad} anios.")

# Limpiar consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Calcular edad
print("Adivinamos tu edad solo sabiendo el anio de nacimiento")
anioNac = int(input("En que anio naciste: "))

Edad(anioNac)