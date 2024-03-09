from datetime import date

ma18 = me18 = 0

for c in range(1, 8):
    idade = int(input('Insira seu ano de nascimento: '))

    if date.today().year - idade >= 18:
        ma18 += 1

    else:
        me18 += 1

print('-=' * 20)
print(f'Maiores de idade: {ma18}\n'
      f'Menores de idade: {me18}')
