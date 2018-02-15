numero = int(input("Escriba un número entero mayor que 1: "))
while numero <= 1:
    numero= int(input(str(numero) + " no es mayor que 1. Inténtelo de nuevo: "))
____copia = numero

print("Descomposición en factores primos: ")
__i= 2
while copia > i:
    while __copia % i == 0:
        copia = copia // i
        print(i)
    i += 1
print(copia)

print()
print("Programa terminado")
