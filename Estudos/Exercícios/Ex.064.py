n = quant = soma = 0
while n != 999:
    n = int(input('Um número [999 para parar]: '))
    if n != 999:
        soma += n
        quant += 1
print('-=' * 20)
print(f'Foram digitados {quant} números e a soma foi {soma}.')
