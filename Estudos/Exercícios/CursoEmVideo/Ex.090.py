aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print('-' * 15)
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'A situação é {aluno["situação"]}')
