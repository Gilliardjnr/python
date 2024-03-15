dados = list()
p = dict()
mulheres = list()
maimed = list()
idade = 0
while True:
    p['nome'] = str(input('Nome: '))
    p['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while p['sexo'] not in 'MF':
        p['sexo'] = str(input('Tente novamente. Sexo [M/F]: ')).upper().strip()[0]
    if p['sexo'] in 'Ff':
        mulheres.append(p['nome'])
    p['idade'] = int(input('Idade: '))
    dados.append(p.copy())
    idade += p['idade']
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Tente novamente. Deseja continuar [S/N]? ')).upper().strip()[0]
    if resp in 'N':
        break
media = idade / len(dados)
if p['idade'] > media:
    maimed.append(p['nome'])
print(dados)

print('-=' * 40)
print(len(dados)) #A)

print(f'{media:.0f}') #B)

print(f'Lista de mulheres: {mulheres}')

print(maimed)


