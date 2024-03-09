peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso / (pow(altura, 2))

print('==' * 18)

if imc < 18.5:
    print('RESULTADO: Você está ABAIXO do peso IDEAL!')

elif 18.5 < imc <= 25:
    print('RESULTADO: Você está no peso IDEAL!')

elif 25 < imc <= 30:
    print('RESULTADO: Você está com SOBREPESO!')

elif 30 < imc < 40:
    print('RESULTADO: Você está com OBESIDADE!')

else:
    print('RESULTADO: Você está com OBESIDADE MÓRBIDA!')

print('==' * 18)
