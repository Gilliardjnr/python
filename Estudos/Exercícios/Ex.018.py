
# Imports:

from math import sin, tan, cos, radians

# Variável:

ang = float(input('Insira o ângulo que deseja converter: '))

# Cálculos

sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

# Exibição na Tela:

print(f'Seno: {sin :.2f} \nCosseno: {cos :.2f} \ntangente: {tan :.2f}')



