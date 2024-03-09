s = cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont += 1
print(f'A soma de todos os {cont} números ímpares entre 1 - 500 é: {s}')

