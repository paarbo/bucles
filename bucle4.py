valor = int(input("¿Cuántos valores va a introducir? "))
if valor>0:
    primer = int(input("Escriba un número: "))
    for i in range(valor - 1):
        num = int(input(f"Escriba un número más grande que {primer}: "))
        if num <= primer:
            print(f"¡{num} no es mayor que {primer}!")
        primer = num  
