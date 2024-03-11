valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if resp not in 'SN':
        resp = str(input('Erro, tente novamente. Deseja continuar [S/N]? ')).upper().strip()[0]
    elif resp in 'N':
        break
print('=' * 30)
print(f'Valores digitados: {valores}'
      f'\nValores pares: {pares}'
      f'\nValores ímpares: {impares}')
