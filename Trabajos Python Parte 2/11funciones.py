# Funciones en Python
# Funciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

# Limpiar consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Operaciones aritmeticas
print("Operaciones Aritmeticas")
x = int(input("a: "))
y = int(input("b: "))

s = suma(x, y)
r = resta(x, y)
m = multiplicacion(x, y)
d = division(x, y)
p = potencia(x, y)

print(f"{x} + {y} = {s}")
print(f"{x} - {y} = {r}")
print(f"{x} * {y} = {m}")
print(f"{x} / {y} = {d}")
print(f"{x} ^ {y} = {p}")
