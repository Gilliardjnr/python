s = cont = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}ª número: '))

    if n % 2 == 0:
        s = s + n
        cont += 1
print(f'Resultado da soma de {cont} números PARES: {s}')
