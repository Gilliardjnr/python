valor_casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o salário: '))
prazo = int(input('Em quantos anos você deseja pagar: '))

prestacao = valor_casa / (prazo * 12)
permitido = salario * 30 / 100

print('-=' * 30)

if prestacao > permitido:
    print('RESULTADO: Seu empréstimo foi negado.', end=' ')
else:
    print('RESULTADO: Seu empréstimo foi autorizado.', end=' ')
print('Tenha um ótimo dia!')

print('-=' * 30)
