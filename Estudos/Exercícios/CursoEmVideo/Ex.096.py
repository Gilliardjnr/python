def areaterreno(a, b):
    area2 = a * b
    print(f'A área do terreno equivale a: {area2}m²')


print('CONTROLE DE TERRENOS')
print('-' * 30)
areaterreno(float(input('Largura: ')), float(input('Comprimento: ')))
