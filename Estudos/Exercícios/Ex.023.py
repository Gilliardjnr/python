# Variável:

number = int(input('Digite um número: '))

# Operações:

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

# Exibição na tela:

print('-=' * 10)
print(f'Analisando o número {number}')
print('-=' * 10)
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
