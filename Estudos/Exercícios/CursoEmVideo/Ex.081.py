valores = list()
five = 'Não'
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if resp not in 'SN':
        resp = str(input('Erro, tente novamente. Deseja continuar [S/N]? ')).upper().strip()
    if 5 in valores:
        five = 'Sim'
    if resp in 'N':
        break
print('=' * 30)
print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'Lista em forma decrescente: {valores}')
if five == 'Sim':
    print(f'O valor 5 foi digitado e está na posição {valores.index(5)}')
else:
    print('O valor 5 não foi digitado!')
