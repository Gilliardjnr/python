def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    from math import factorial
    fact = factorial(n)
    cont = n - 1
    if show:
        for c in range(n, 0):
            while cont != 0:
                print(f'{n} x {cont}')
                cont -= 1
    else:
        print(fact)

fatorial(3, True)



