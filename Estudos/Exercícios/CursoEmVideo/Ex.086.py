valores = list()
provisoria = list()
for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite um valor: '))
        provisoria.append(n)
    valores.append(provisoria[:])
    provisoria.clear()
for c, n in enumerate(valores):
    print(f'{valores[c]}')
