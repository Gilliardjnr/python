def voto(a):
    from datetime import datetime
    idade = datetime.today().year - a
    global situacao
    situacao = ''
    if idade < 16:
        situacao = 'NÃO VOTA!'
    elif 16 > idade < 18:
        situacao = 'VOTO OPCIONAL!'
    elif 18 >= idade < 65:
        situacao = 'VOTO OBRIGATÓRIO!'
    elif idade > 65:
        situacao = 'VOTO OPCIONAL!'
    resultado = f'Com {idade} anos: {situacao}'
    print(resultado)
    return resultado


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
print(situacao)
