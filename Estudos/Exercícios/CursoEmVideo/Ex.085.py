numeros = list()
par = list()
impar = list()
for c in range(0, 7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()
numeros.append(par)
numeros.append(impar)
print('=' * 30)
print(numeros)
