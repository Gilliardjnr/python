# Variáveis

largura = float(input('Insira a largura da parede (m): '))
altura = float(input('Insira a altura da parede (m): '))

# Cálculos

area = largura * altura
tinta = area / 2

# Exibição

print(f'É necessário {tinta} litros de tinta para pintar {area}m²')
