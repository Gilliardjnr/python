valores = list()
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp not in 'SN':
         resp = str(input('Resposta inválida, tente novamente. Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break
print('=' * 35)
valores.sort()
print(f'Os valores em ordem crescente são: {valores}')
