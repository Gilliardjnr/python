# Variável:
phrase = str(input('Digite uma frase: ')).lower().strip()

# Impressão na tela:
print(f"""Contagem de 'a': {phrase.count('a')}
primeira vez: {phrase.find('a') + 1}
última vez: {phrase.rfind('a') + 1}
""")
