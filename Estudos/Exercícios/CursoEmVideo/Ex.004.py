# Variável:

a = input('Digite algo: ')

# Exibição na tela:

print(f'Seu tipo primitivo: {type(a)}')

print(20 * '-=')

print(f'É alfabético: {a.isalpha()}')
print(f'É numérico: {a.isnumeric()}')
print(f'É alfanumérico: {a.isalnum()}')
print(f'É somente espaços: {a.isspace()}')
print(f'É capitalizado: {a.istitle()}')
