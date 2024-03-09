n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

print('-=' * 20)

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não há valor maior. Ambos são iguais!')

print('-=' * 20)
