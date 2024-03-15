from datetime import datetime
civil = dict()
civil['nome'] = str(input('Nome: '))
civil['nascimento'] = int(input('Ano de nascimento: '))
civil['carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))
civil['idade'] = datetime.today().year - civil['nascimento']
if civil['carteira'] != 0:
    civil['contratação'] = int(input('Ano de contratação: '))
    civil['salario'] = float(input('Salário: R$'))
    contrato = datetime.today().year - civil['contratação']
    civil['aposentadoria'] = (35 - contrato) + civil['idade']
print('=' * 20)
for k, v in civil.items():
    print(f'{k}: {v}')
print('=' * 20)
