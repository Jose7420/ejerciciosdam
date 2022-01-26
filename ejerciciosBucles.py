# ejercicio 2

print("Ejercicio 2")

print("Dime un numero entero")
cuenta = int(input("-->"))


while(cuenta != 0):

    print("%d, " % cuenta)
    cuenta -= 1


# ejercicio 3

print("Ejercicio 3")

print("Dime un numero entero")
num = int(input("-->"))

for x in range(num):
    if(x % 2):
        print(x)


# ejercicio 4
print("\nEjercicio 4 \n")

for a in range(1, 11):
    print("\nla tabla del %d " % a)
    for b in range(1, 11):
        print("%d X %d = %d " % (a, b, (a*b)))


# ejercicio 5
print("\nEjerccio 5\n")
print("Para Terminar escriba Salir")
while True:

    entrada = input()

    if(entrada.lower() != "salir"):
        print("%s" % entrada)
