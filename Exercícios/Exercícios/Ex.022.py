name = str(input('Digite seu nome completo: '))

print('-=' * 20)
print(f'Escrito: {name}')
print('-=' * 20)

contagem = name.count(' ')
divisao = name.split()

print(f"""Maiúsculo: {name.upper()}
Minúsculo: {name.lower()}
Tamanho: {len(name) - contagem} digitos
Primeiro nome: {len(divisao[0])} digitos""")


