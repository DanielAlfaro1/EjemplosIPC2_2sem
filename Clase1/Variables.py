variable1 = "Hola pollitos"     #variable tipo str
variable2 = 2
variable3 = 2023                #variable tipo int
a = 2.3                         #variable tipo float
b = False                       #variable tipo bool
c = True                        #varialbe tipo bool
lista = ["Año", variable3, "Semestre"+str(variable2), variable1] #variables tipo list

print(variable1)
print(variable2, type(variable2))
print([(x, type(x)) for x in lista])

print(variable3)
print(a, type(a))
print(b, type(b))
print(c, type(c))

a = "Hola mundo"
print(a, type(a))

print(lista, type(lista))

print(len(lista))
print(len(a))