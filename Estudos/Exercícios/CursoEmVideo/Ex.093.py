jogador = dict()
gols = list()
totalg = 0
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantas partidas: '))
for c in range(1, jogador['partidas'] + 1):
    g = (int(input(f'Quantos gols na partida {c}? ')))
    totalg += g
    gols.append(g)
jogador['gols'] = gols
jogador['total'] = totalg
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for p, g in enumerate(gols):
    print(f' => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
