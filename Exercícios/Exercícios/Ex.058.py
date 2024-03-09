from random import randint
computador = randint(0, 10)
jogador = tentativas = 0
while jogador != computador:
    jogador = int(input('Insira sua tentativa [0 - 10]: '))
    if jogador != computador:
        print('Infelizmente você não conseguiu... Tente mais uma vez!')
    tentativas += 1
    print('-=' * 27)
print(f'Parabéns, você me venceu com {tentativas} tentativas!')
