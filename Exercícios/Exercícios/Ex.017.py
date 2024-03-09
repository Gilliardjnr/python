
# Variáveis:

co = float(input('Insira a medida do cateto oposto: '))
ca = float(input('Insira a medida do cateto adjacente: '))

# Cálculos:

hip = pow(co, 2) + pow(ca, 2)
hip2 = pow(hip, 1/2)

# Exibição na tela:f

print(f'A hipotenusa corresponderá a: {hip2 :.2f}')
