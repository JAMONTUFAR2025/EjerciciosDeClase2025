# notas de 4 parciales en un arreglo
import os
os.system('cls' if os.name == 'nt' else 'clear')

notas=[0,0,0,0]
print("Ingrese Notas")
notas[0]=int(input("Nota 1: "))
notas[1]=int(input("Nota 2: "))
notas[2]=int(input("Nota 3: "))
notas[3]=int(input("Nota 4: "))

print(notas)

sumaNotas=notas[0]+notas[1]+notas[2]+notas[3]
promedio=sumaNotas/4

print("Promedio=",promedio)

if promedio>=70:
    print("Aprobó")
else:
    print("Reprobó!")

## calificaciones 
# 00-49 NO TIENE DERECHO A RECUPERACION
# 50-69 NO SATISFACTORIO
# 70-80 BUENO
# 81-90 MUY BUENO
# 91-100 EXCELENTE

if promedio>=0 and promedio<50:
    print ("NO TIENE DERECHO A RECUPERACION")
elif promedio>=50 and promedio<70:
    print("NO SATISFACTORIO")
elif promedio>=70 and promedio<81:
    print("BUENO")

if promedio>=0 and promedio<=49:
    print ("NO TIENE DERECHO A RECUPERACION")

if promedio>=50 and promedio<=69:
    print("NO SATISFACTORIO")
    
if promedio>=70 and promedio<81:
    print("BUENO")