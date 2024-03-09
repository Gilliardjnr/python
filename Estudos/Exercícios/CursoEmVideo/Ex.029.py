v = float(input('Insira a velocidade do carro: '))

multa = (v - 80) * 7

print('-=' * 10)
if v > 80:
    print('Você foi multado!', end=' ')
    print(f'O valor da sua multa equivale a: R${multa}')

else:
    print('Pode seguir em frente!')
