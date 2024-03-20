def voto(a):
    from datetime import datetime
    global idade
    idade = datetime.today().year - a
    situaçao = ''
    if idade < 16:
        situaçao = 'NÃO VOTA!'
    elif 16 > idade < 18:
        situaçao = 'VOTO OPCIONAL!'
    elif 18 >= idade < 65:
        situaçao = 'VOTO OBRIGATÓRIO!'
    elif idade > 65:
        situaçao = 'VOTO OPCIONAL!'
    naosei = situaçao
    return naosei


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

