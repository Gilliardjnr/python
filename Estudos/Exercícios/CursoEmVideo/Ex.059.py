from time import sleep
opçao = 0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('''O que você deseja fazer com os números: 

[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa ''')

while opçao != 5:
    print('-=' * 15)
    opçao = int(input('Insira uma opção: '))
    print('-=' * 15)

    if opçao == 1:
        soma = n1 + n2
        print(f'A Soma entre {n1} + {n2} = {soma}')
    elif opçao == 2:
        multi = n1 * n2
        print(f'A Multiplicação entre {n1} * {n2}: {multi}')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O Maior entre {n1} e {n2} = {maior}')
    elif opçao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('Finalizando', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
sleep(1)
print(' Obrigado, volte sempre!')
