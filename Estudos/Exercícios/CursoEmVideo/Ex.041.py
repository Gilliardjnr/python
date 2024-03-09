from datetime import datetime

ano = int(input('Insira seu ano de nascimento: '))

print('-=' * 17)

if datetime.today().year - ano <= 9:
    print('RESULTADO: Sua categoria é MIRIM!')

elif 9 < datetime.today().year - ano <= 14:
    print('RESULTADO: Sua categoria é INFANTIL!')

elif 14 < datetime.today().year - ano <= 19:
    print('RESULTADO: Sua categoria é JUNIOR')

elif 19 < datetime.today().year - ano <= 25:
    print('RESULTADO: Sua categoria é SÊNIOR!')

else:
    print('RESULTADO: Sua categoria é MASTER!')
