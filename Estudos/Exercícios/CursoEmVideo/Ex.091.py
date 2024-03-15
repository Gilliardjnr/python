from random import randint
from time import sleep
jogos = dict()
jogos['jogador 1'] = randint(1, 6)
jogos['jogador 2'] = randint(1, 6)
jogos['jogador 3'] = randint(1, 6)
jogos['jogador 4'] = randint(1, 6)
for k, v in jogos.items():
    print(f'{k}: {v}')
    sleep(1)

