from random import randint
numeros = list()


def sorteia(sp=0):
    for g in range(0, 5):
        n = randint(1, 10)
        if n % 2 == 0:
            sp += n
        numeros.append(n)


#def somapar():
#    print(sp)



sorteia()
print(numeros, sp)
