import random

print(random.random())

for indice in range(10): #for int i = 0; i < 10; i++
    print(indice)
    print(random.random())

def No_Repito(numero):
    print("No repito dos veces")
    if int(numero) % 2 == 0:
        print("Que dijo?")
        print("No repito dos veces")
    return numero

print(No_Repito(round(random.random()*10)))