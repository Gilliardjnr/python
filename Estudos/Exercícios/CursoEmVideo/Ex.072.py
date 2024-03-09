numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
n = int(input('Escolha um número entre 0 - 20: '))
while True:
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}!')
        break
    else:
        n = int(input('Tente novamente! Insira um número entre 0 - 20: '))

