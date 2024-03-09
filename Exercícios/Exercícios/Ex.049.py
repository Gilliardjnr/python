n = int(input('Digite um número para ver sua tabuada: '))

print('-=' * 15)

for c in range(1, 11):
    print(f'{n} * {c} = {n * c}')
