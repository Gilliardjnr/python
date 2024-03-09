# Variáveis:

km = float(input('Insira a quilometragem percorrida: '))
day = float(input('Insira a quantidade de dias de aluguel: '))

# Cálculos:

day_price = day * 60
km_price = km * 0.15

# Exibição na tela:

print(f'Com {day :.0f} dias de uso, e {km}km percorridos, o preço final será de R${day_price + km_price :.2f}')

