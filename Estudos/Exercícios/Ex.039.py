from datetime import datetime

ano = int(input('Insira seu ano de nascimento: '))

print('=-=' * 15)

if datetime.today().year - ano < 18:
    print('RESULTADO: Você ainda vai se alistar.')
    falta = 18 - (datetime.today().year - ano)
    print(f'Faltam {falta} ano/s para você se alistar')

elif datetime.today().year - ano == 18:
    print('RESULTADO: Está na hora de se alistar')

else:
    print('RESULTADO: Você passou do tempo de se alistar.')
    passou = (datetime.today().year - ano) - 18
    print(f'Você atrasou seu alistamente por {passou} ano/s')
