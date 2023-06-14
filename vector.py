"""Módulo com as funções de manipulação de vetores."""


def norma(x: list[float]) -> float:
    """Calcula a norma de um vetor"""
    norma_vertor = 0
    somas = 0
    if x == []:
        return None
    else:
        for number in x:
            quadrados = number * number
            somas += quadrados
        
        norma_vertor = somas ** 0.5
        return norma_vertor

    # TODO: implementar
    # a norma de um vetor [3, 4] é 5
    # a norma de um vetor [1, 2, 4] é 4.58257569495584
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos do vetor
    # se o vetor estiver vazio retorne None


def soma(x: list[float], y: list[float]) -> list[float]:
    """Soma dois vetores"""
    somas = []
    if len(x) == len(y):
        for i in range(len(x)):
            s = x[i] + y[i]
            somas.append(s)
        return somas
    else:
        return None

    # TODO: implementar
    # a soma de dois vetores [1, 2, 4] + [2, 3, 4] é [3, 5, 8]
    # a soma só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None


def multiplicação_por_escalar(vetor: list[float], escalar: float) -> list[float]:
    """Multiplica um vetor por um escalar"""
    mult_esc = []
    for i in vetor:
        p = i * escalar
        mult_esc.append(p)
    return mult_esc

    # TODO: implementar
    # a multiplicação de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]


def produto_interno(x: list[float], y: list[float]) -> float:
    """Calcula o produto interno de dois vetores"""
    produto = 0
    if len(x) == len(y):
        for i in range(len(x)):
            a = x[i] * y[i]
            produto += a
        return produto
    else:
        return None
    # TODO: implementar
    # o produto interno de dois vetores [1, 2, 4] e [2, 3, 4] é 24
    # o produto interno consiste em multiplicar os elementos de mesmo índice e somar os resultados
    # a multiplicação só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    # caso os vetores sejam vazios o resultado é 0


def produto_vetorial(x: list[float], y: list[float]) -> list[float]:
    """Calcula o produto vetorial de dois vetores"""
    produto = []
    if len(x) == 3 and len(y) == 3:
        for i in range(len(x)):
            for j in range(len(y)):
                pass        
        return produto
    else:
        return None
    
    # TODO: implementar
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None


def produto_diádico(x: list[float], y: list[float]) -> list[list[float]]:
    """Calcula o produto diádico de dois vetores"""
    produto = []
    if len(x) == len(y):
        return produto
    else:
        return None
    # TODO: implementar
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
