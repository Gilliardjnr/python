d = float(input('Insira a distância da viagem: '))

km = 0.50

if d > 200:
    km = 0.45

print(f'Para {d}km, oorçamento final será: R${d * km}')
