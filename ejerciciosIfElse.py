# ejercicio 2
print("Ejercicio 2")

print("Dime tu edad")
edad = int(input("--> "))

if(edad > 17):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# ejercicio  3
print("Ejercicio 3")
key = "contraseña"

print("Contraseña")
cot = input("--> ")

if(cot.lower() == key.lower()):
    print("es correcta")

else:
    print("No es correcta")


# ejercicio 4
print("ejercicio 4")

print("Dime un numero entero")
num = int(input("--> "))

if(not(num % 2)):
    print("Es par")
else:
    print("Es impar")

# ejercicio 5
print("Ejericio 5")

print("Dime un numero para el dividendo")
num1 = int(input("--> "))

print("Dime un numero para el divisor")
num2 = int(input("--> "))

if(num2 == 0):
    print("no se puede dividir por cero")

else:
    result = num1/num2
    print("el resultado es %d " % result)
