num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] - BINÁRIO
[ 2 ] - OCTAL
[ 3 ] - HEXADECIMAL
''')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a: {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a: {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a: {hex(num)[2:]} ')
else:
    print('Opção inválida. Tente novamente.')
