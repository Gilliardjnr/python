# Variável:
name = str(input('Digite o seu nome: ')).strip()

# Exibição na tela:
print('-=' * 10)
print(f'Seu nome tem Silva? {"silva" in name.lower()}')
