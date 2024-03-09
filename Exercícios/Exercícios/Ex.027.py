# Variável:
name = str(input('Digite o seu nome completo: ')).strip()

# "Operações":
divisao = name.split()

# Exibição na tela:
print('-=' * 15)
print(f"""Primeiro: {divisao[0]}
Último: {divisao[len(divisao) - 1]}
""")


