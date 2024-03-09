m18 = mulher = homem = 0
while True:
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()
    if sexo not in 'MmFf':
        print('Resposta inválida! Tente novamente...')
        break
    resp = str(input('Deseja continuar? ')).strip().upper()
    if idade >= 18:
        m18 += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if sexo in 'Mm':
        homem += 1
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'Pessoa cadastradas maiores de idade: {m18}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres com menos de 20 anos: {mulher}')
