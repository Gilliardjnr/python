salario = float(input('Insira o seu salário: '))


if salario > 1.250:
    aumento = (salario * 10 / 100) + salario
    perc = '10%'

else:
    aumento = (salario * 15 / 100) + salario
    perc = '15%'

print(f'Com salário {salario} Você terá direito à {perc} de aumento. \nSeu salário final será de R${aumento}')
