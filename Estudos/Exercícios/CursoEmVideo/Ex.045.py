from random import choice

print(f'{"VAMOS JOGAR JOKENPÔ" :=^50}')

print("""
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
""")

jogador = int(input('Faça sua escolha: '))
computador = choice(['Pedra', 'Papel', 'Tesoura'])

if jogador == 1:
    jogador = 'Pedra'

elif jogador == 2:
    jogador = 'Papel'

else:
    jogador = 'Tesoura'

# Condições de vitória

print(f'{"RESULTADO" :=^30}')

if computador == 'Pedra':
    if jogador == 'Papel':
        print('Você venceu...')

    elif jogador == 'Tesoura':
        print('Eu venci!')

    else:
        print('Velha!')

elif computador == 'Papel':
    if jogador == 'Pedra':
        print('Eu venci!')

    elif jogador == 'Tesoura':
        print('Você venceu...')

    else:
        print('Velha!')

else:
    if jogador == 'Pedra':
        print('Você venceu...')

    elif jogador == 'Papel':
        print('Eu venci!')

    else:
        print('Velha')

print('=' * 30)

print(f'Pois eu escolhi {computador}, e você escolheu {jogador}!')
