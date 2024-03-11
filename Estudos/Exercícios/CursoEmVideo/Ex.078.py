numeros = list()
maior = menor = 0
for c in range(0, 5):
    n = int(input(f'Digite um número para posição {c}: '))
    numeros.append(n)
print('=' * 35)
print(numeros)
print('=' * 35)
for v in range(0, 1):
    for c, n in enumerate(numeros):
        print(f'O maior número é: {max(numeros)} e está na posição {c}')


# print(max(numeros))
# print(min(numeros))
