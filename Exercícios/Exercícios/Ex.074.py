from random import randint
numeros = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
organizado = sorted(numeros)
print(f'Números adicionados: {numeros}')
print('=' * 40)
for n in range(0, 5):
    print(f'{n + 1}º número: {numeros[n]}')
print('=' * 15)
print(f'Menor número: {organizado[0]}')
print(f'Maior número: {organizado[4]}')
