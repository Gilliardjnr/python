pessoas = list()
provisoria = list()
leve = pesado = 0
while True:
    nome = str(input('Insira o nome: ')).strip()
    peso = float(input('Insira o peso: '))

    provisoria.append(nome)
    provisoria.append(peso)
    pessoas.append(provisoria[:])
    provisoria.clear()

    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'SN':
         resp = str(input('Tente novamente. Deseja continuar [S/N]? ')).strip().upper()[0]

    if resp in 'N':
        break
print('=' * 30)
print(f'Número de pessoas cadastradas: {len(pessoas)} pessoas.')
for p in pessoas:
    if p == 0:
        leve = pesado = p[0][1]
    #if p > 1:
print(pessoas)
print(leve)
print(pesado)
