soma = quantidade = 0
while True:
    n = int(input('Digite um número [999  para parar]: '))
    if n == 999:
        break
    soma += n
    quantidade += 1
print('-=' * 30)
print(f'A soma dos {quantidade} números que foram digitados equivale a: {soma}')
