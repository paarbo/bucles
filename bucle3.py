num1=int(input("Escribe un numero: "))
num2=int(input("Otro numero: "))

while (num1<num2):
    num1=num2
    num2=int(input("Otro numero "+ str(num1)+ ": "))
print ("No es mayor",num1,"que", str(num2) + " ")
print("Programa terminado")
