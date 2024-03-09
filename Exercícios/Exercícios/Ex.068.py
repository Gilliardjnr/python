from random import randint
vencedor = ''
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    computador = randint(1, 11)
    num = int(input('Insira um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('-=' * 20)
    soma = computador + num
    if escolha not in 'PI':
        print('Resposta inválida, tente novamente!')
    elif escolha in 'Pp':
        escolha = 'Par'
    elif escolha in 'Ii':
        escolha = 'Ímpar'
    if soma % 2 == 0:
        vencedor = 'Par'
    else:
        vencedor = 'Ímpar'
    print(f'Você jogou {num} e o computador {computador}. Total de {soma}, deu {vencedor}!')
    if escolha == vencedor:
        print('VOCÊ VENCEU!', end =' ')
        print('vamos jogar novamente...')
        print('-=' * 20)
        cont += 1
    else:
        print(f'VOCÊ PERDEU! Você venceu {cont} vezes.')
        break


