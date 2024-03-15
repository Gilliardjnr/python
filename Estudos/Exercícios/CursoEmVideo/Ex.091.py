from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
ranking = list()
jogos['jogador 1'] = randint(1, 6)
jogos['jogador 2'] = randint(1, 6)
jogos['jogador 3'] = randint(1, 6)
jogos['jogador 4'] = randint(1, 6)
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
