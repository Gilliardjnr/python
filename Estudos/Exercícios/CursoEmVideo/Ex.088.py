from random import randint
jogos = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
quant = int(input('Quantos jogos você deseja gerar? '))
for c, j in enumerate(jogos):
    print(f'{jogos[c]}', end=' ')
