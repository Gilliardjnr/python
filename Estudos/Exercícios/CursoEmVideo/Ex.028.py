# Import de Lib:
from random import randint

# Variável:
e = int(input('Escolha um número de 0 a 5: '))

print('-=' * 15)

# "Operações:
n = randint(0, 5)

print(f'O número sorteado foi: {n}')

if e == n:
    print('Parabéns, Você acertou!')
else:
    print('Errou! Tente novamente.')

