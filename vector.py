"""Módulo com as funções de manipulação de vetores."""

from tipos import Escalar, Matriz, Vetor


def norma(vetor_1: Vetor) -> Escalar:
    """Calcula a norma de um vetor"""
    norma_vertor = 0
    somas = 0
    if vetor_1 == []:
        return None
    else:
        for number in vetor_1:
            quadrados = number * number
            somas += quadrados
        norma_vertor = somas**0.5
        return norma_vertor

    # : implementar
    # a norma de um vetor [3, 4] é 5
    # a norma de um vetor [1, 2, 4] é 4.58257569495584
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos do vetor
    # se o vetor estiver vazio retorne None


def soma(vetor_1: Vetor, vetor_2: Vetor) -> Vetor:
    """Soma dois vetores"""
    soma_ = []
    if len(vetor_1) == len(vetor_2):
        for i, _ in enumerate(vetor_1):
            soma__ = vetor_1[i] + vetor_2[i]
            soma_.append(soma__)
        return soma_
    else:
        return None

    # : implementar
    # a soma de dois vetores [1, 2, 4] + [2, 3, 4] é [3, 5, 8]
    # a soma só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None


def multiplicacao_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplica um vetor por um escalar"""
    mult_esc = []
    for i in vetor:
        produto__ = i * escalar
        mult_esc.append(produto__)
    return mult_esc

    # : implementar
    # a multiplicação de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]


def produto_interno(vetor_1: Vetor, vetor_2: Vetor) -> float:
    """Calcula o produto interno de dois vetores"""
    produto = 0
    if len(vetor_1) == len(vetor_2):
        for i, _ in enumerate(vetor_1):
            prod = vetor_1[i] * vetor_2[i]
            produto += prod
        return produto
    else:
        return None
    # : implementar
    # o produto interno de dois vetores [1, 2, 4] e [2, 3, 4] é 24
    # o produto interno consiste em multiplicar os elementos de mesmo índice e somar os resultados
    # a multiplicação só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    # caso os vetores sejam vazios o resultado é 0


def produto_vetorial(vetor_1: Vetor, vetor_2: Vetor) -> Vetor:
    """Calcula o produto vetorial de dois vetores"""
    produto = []
    if len(vetor_1) == 3 and len(vetor_2) == 3:
        produto_1 = (vetor_1[1] * vetor_2[2]) - (vetor_1[2] * vetor_2[1])
        produto_2 = (vetor_1[2] * vetor_2[0]) - (vetor_1[0] * vetor_2[2])
        produto_3 = (vetor_1[0] * vetor_2[1]) - (vetor_1[1] * vetor_2[0])
        produto.append(produto_1)
        produto.append(produto_2)
        produto.append(produto_3)

        return produto
    else:
        return None
    # : implementar
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None


def produto_diadico(vetor_1: Vetor, vetor_2: Vetor) -> Matriz:
    """Calcula o produto diádico de dois vetores"""
    produto = []
    if len(vetor_1) == len(vetor_2):
        for i, _ in enumerate(vetor_1):
            produto.append([])
            for j, _ in enumerate(vetor_2):
                produto__ = vetor_1[i] * vetor_2[j]
                produto[i].append(produto__)
        return produto
    else:
        return None
    # : implementar
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
