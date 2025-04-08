# Area y Volumen de Figuras Geometricas
# Limpiar consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Constantes
PI = 3.1416

# Funciones
def AreaYVolumenDeConoTruncado(r1, r2, g, h):
    a = PI * (r1 ** 2 + r2 ** 2 + g * (r1 + r2))
    a = round(a, 2)
    v = ((h * PI) * (r1 ** 2 + r2 ** 2 + r1 * r2)) / 3
    v = round(v, 2)

    return a, v

def AreaYVolumenDeEsfera(r):
    a = 4 * PI * r ** 2
    a = round(a, 2)
    v = (4 * PI * r ** 3) / 3
    v = round(v, 2)

    return a, v

def AreaYVolumenDeCilindro(r, h):
    a = 2 * PI * r * (r + h)
    a = round(a, 2)
    v = PI * r ** 2 * h
    v = round(v, 2)

    return a, v

def ImprimirAreaYVolumen(a, v):
    print(f"A = {a} cm^2.")
    print(f"V = {v} cm^3.")

# Calcular Area y Volumen de Figuras Geometricas
# Cono Truncado
print("\nAREA Y VOLUMEN DE UN CONO TRUNCADO")
print("A = π * [r1 ^ 2 + r2 ^ 2 + g * (r1 + r2)]")
print("V = [(h * π) * (r1 ^ 2 + r2 ^ 2 + r1 * r2)] / 3")
r1 = float(input("r1: "))
r2 = float(input("r2: "))
g = float(input("g: "))
h = float(input("h: "))

a, v = AreaYVolumenDeConoTruncado(r1, r2, g, h)
ImprimirAreaYVolumen(a, v)

print("\nAREA Y VOLUMEN DE UNA ESFERA")
print("A = 4 * π * r ^ 2")
print("V = (4 * π * r ^ 3) / 3")
r = float(input("r: "))

a, v = AreaYVolumenDeEsfera(r)
ImprimirAreaYVolumen(a, v)

print("\nAREA Y VOLUMEN DE UN CILINDRO")
print("A = 2 * π * r * (r + h)")
print("V = π * r ^ 2 * h")
r = float(input("r: "))
h = float(input("h: "))

a, v = AreaYVolumenDeCilindro(r, h)
ImprimirAreaYVolumen(a, v)