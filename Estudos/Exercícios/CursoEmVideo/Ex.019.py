# Importando LIB

from random import choice

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))

# Randomizando:

alunos = (a1, a2, a3, a4)
escolhido = choice(alunos)

# Exibição na tela:

print(f'{"RESULTADO" :=^50}')
print(f'Dentre os alunos {a1}, {a2}, {a3} e {a4}. \nO escolhido foi: {escolhido}')


