n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('-=' * 15)
print(f'Sua média equivale a: {media}')
print('-=' * 15)

if media < 5.0:
    print('RESULTADO: REPROVADO!')

elif 5.0 < media < 6.9:
    print('RESULTADO: RECUPERAÇÃO!')

else:
    print('RESULTADO: APROVADO!')
