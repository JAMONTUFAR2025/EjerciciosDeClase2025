# Limpiar Terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Area y Volumen
print("AREA Y VOLUMEN DE FIGURAS GEOMETRICAS")

# Constante PI
PI = 3.1416

# Cono Truncado
print("CONO TRUNCADO")
print("Area = π * [radio1 ^ 2 + radio2 ^ 2 + generatriz * (radio1 + radio2)]")
print("Volumen = [(altura * π) * (radio1 ^ 2 + radio2 ^ 2 + radio1 * radio2)] / 3")
radio1 = float(input("\nDigite el valor del radio menor en centimetros: "))
radio2 = float(input("Digite el valor del radio mayor en centimetros: "))
generatriz = float(input("Digite el valor de la generatriz en centimetros: "))
altura = float(input("Digite el valor de la altura en centimetros: "))

area = PI * (radio1 ** 2 + radio2 ** 2 + generatriz * (radio1 + radio2))
area = round(area, 2)
volumen = ((altura * PI) * (radio1 ** 2 + radio2 ** 2 + radio1 * radio2)) / 3
volumen = round(volumen, 2)

print(f"El Area del Cono Truncado es {area} centimetros cuadrados.")
print(f"El Volumen del Cono Truncado es {volumen} centimetros cubicos.")

# Esfera
print("\nAREA Y VOLUMEN DE UNA ESFERA")
print("Area = 4 * π * radio ^ 2")
print("Volumen = (4 * π * radio ^ 3) / 3")
radio = float(input("Digite el valor del radio en centimetros: "))

area = 4 * PI * radio ** 2
area = round(area, 2)
volumen = (4 * PI * radio ** 3) / 3
volumen = round(volumen, 2)

print(f"El Area de la Esfera es {area} centimetros cuadrados.")
print(f"El Volumen de la Esfera es {volumen} centimetros cubicos.")

# Cilindro
print("\nAREA Y VOLUMEN DE UN CILINDRO")
print("Area = 2 * π * radio * (radio + altura)")
print("Volumen = π * radio ^ 2 * altura")
radio = float(input("Digite el valor del radio en centimetros: "))
altura = float(input("Digite el valor de la altura en centimetros: "))

area = 2 * PI * radio * (radio + altura)
area = round(area, 2)
volumen = PI * radio ** 2 * altura
volumen = round(volumen, 2)

print(f"El Area del Cilindro es {area} centimetros cuadrados.")
print(f"El Volumen del Cilindro es {volumen} centimietros cubicos.")