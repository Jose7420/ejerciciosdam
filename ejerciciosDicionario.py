# ejercicio 2
from imp import init_frozen
print("Ejercicio 2")


asignatura1 = ["matematicas", "fisica", "quimica", "historia", "lengua"]
print(asignatura1[0:len(asignatura1)])


asignatura2 = set(["matematicas", "fisica", "quimica", "historia", "lengua"])
print(asignatura2)

# ejercicio 3
print("Ejercicio 3")

for x in range(0, len(asignatura1)):
    print("Yo estudio "+asignatura1[x])


# ejercicio 4
print("Ejercicio 4")

print("que asignatura cursas: ")
asig = input(" >")

if (asig in asignatura2):
    print("esta en el set ")
else:
    print("No esta en el set")


# ejercicio 5
print("Ejercicio 5")
numeros = [1, 2, 3]
cadena = ["hola", "mundo"]

numeros.append(9)
print(numeros)

cadena.append("Espacio")
print(cadena)


# ejercicio 6
print("Ejercicio 6")
a = {"Jake", "John", "Eric"}

b = {"John", "Jill"}

c = a.difference(b)
print(c)


# ejercicio 7
print("Ejercicio 7")

l = set()
for i in range(1, 6):
    l.add(pow(i, 2))
print(l)

lo = set()
[lo.add(pow(x, 2)) for x in range(1, 6)]

print(lo)

# ejercicio 8
print("Ejercicio 8")
