while True:
    tabuada = int(input('Insira um número para ver a tabuada: '))
    if tabuada < 0:
        break
    print('-=' * 20)
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('-=' * 20)
print('-=' * 20)
print('Obrigado por sua participação, volte sempre!')
