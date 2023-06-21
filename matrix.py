"""Módulo com as funções de manipulação de matrizes."""

from tipos import Escalar, Matriz


def soma(matriz_1: Matriz, matriz_2: Matriz) -> Matriz:
    soma_matrizes = []
    if matriz_1 == [] and matriz_2 == []:
        return []
    else:
        if len(matriz_1) == len(matriz_2) and len(matriz_1[0]) == len(matriz_2[0]):
            for i, _ in enumerate(matriz_1):
                soma_matrizes.append([])
                for j, _ in enumerate(matriz_1[0]):
                    somas = matriz_1[i][j] + matriz_2[i][j]
                    soma_matrizes[i].append(somas)
            return soma_matrizes
        else:
            return None


def multiplicacao_por_escalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplica uma matriz por um escalar"""
    result = []
    for line in matriz:
        newline = []
        for element in line:
            newline.append(element * escalar)

        result.append(newline)

    return result


def multiplicacao(matriz_1: Matriz, matriz_2: Matriz) -> Matriz:
    """Multiplica duas matrizes"""
    if matriz_1 == []:
        return matriz_1
    if len(matriz_1) != len(matriz_2[0]):
        return None
    else:
        C = [[0 for _ in range(len(matriz_2[0]))] for _ in range(len(matriz_1))]
        for i in range(len(matriz_1)):
            for j in range(len(matriz_2[0])):
                for k in range(len(matriz_1[0])):
                    C[i][j] += matriz_1[i][k] * matriz_2[k][j]
        return C


def norma(matriz_1: Matriz) -> float:
    """Calcula a norma de uma matriz"""
    lista = []
    norm = 0
    for i in matriz_1:
        for j in i:
            quociente = j * j
            lista.append(quociente)
    for number in lista:
        norm += number
    norma_final = norm**0.5
    return norma_final


def eh_simetrica(matriz_1: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    if matriz_1 == []:
        return True
    if len(matriz_1) == len(matriz_1[0]) and transposta(matriz_1) == matriz_1:
        return True
    else:
        return False
    # : implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta


def transposta(matriz_1: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    transposta_ = []
    if matriz_1 == []:
        return []
    for i, _ in enumerate(matriz_1[0]):
        transposta_.append([])
        for j, _ in enumerate(matriz_1):
            transposta_[i].append(matriz_1[j][i])

    return transposta_
    #: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]
