sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    print('Valor não suportado. Tente novamente!')
    sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()
print('Obrigado por sua colaboração. Volte sempre!')
