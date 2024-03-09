preco = float(input('Insira o valor do produto: '))

print('==' * 30)

print("""
[ 1 ] - Á vista dinheiro cheque: 10% desconto.
[ 2 ] - Á vista no cartão: 5% de desconto.
[ 3 ] - 2x no cartão: preço normal.
[ 4 ] - 3x ou mais no cartão: 20% de juros
""")

print('==' * 30)

pagamento = int(input('Insira a forma de pagamento: '))

print('==' * 30)

if pagamento == 1:
    desconto = preco - (preco * 10 / 100)
    print(f'O preço final será de: R${desconto}')

elif pagamento == 2:
    desconto = preco - (preco * 5 / 100)
    print(f'O preço final será de: R${desconto}')

elif pagamento == 3:
    print(f'O produto se manterá no mesmo preço: R${preco}')

elif pagamento == 4:
    juros = preco + (preco * 20 / 100)
    print(f'O preço do produto passará a ser R${juros}')

else:
    print('Esta forma de pagamento não está disponível. Tente novamente!')
