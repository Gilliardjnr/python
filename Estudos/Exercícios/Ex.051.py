start = int(input('Primeiro termo: '))
razao = int(input('razão: '))
decimo = start + (10 - 1) * razao

for c in range(start, decimo + razao, razao):
    print(f'{c}')
