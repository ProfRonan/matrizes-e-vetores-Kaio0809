"""Módulo com as funções de manipulação de matrizes."""

from tipos import Escalar, Matriz


def soma(x: Matriz, y: Matriz) -> Matriz:
    soma_matrizes = []
    if x == [] and y == []:
        return []
    else:
        if len(x) == len(y) and len(x[0]) == len(y[0]):
            for i in range(len(x)):
                soma_matrizes.append([])
                for j in range(len(x[0])):
                    somas = x[i][j] + y[i][j]
                    soma_matrizes[i].append(somas)
            return soma_matrizes
        else:
            return None


def multiplicação_por_escalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplica uma matriz por um escalar"""
    result = []
    for line in matriz:
        newLine = []
        for element in line:
            newLine.append(element * escalar)

        result.append(newLine)

    return result


def multiplicação(x: Matriz, y: Matriz) -> Matriz:
    """Multiplica duas matrizes"""
    if x == []:
        return x
    if len(x) != len(y[0]):
        return None

    else:
        C = [[0 for _ in range(len(y[0]))] for _ in range(len(x[0]))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(x[0])):
                    C[i][j] += x[i][k] * y[k][j]
        return C


def norma(x: Matriz) -> float:
    """Calcula a norma de uma matriz"""
    l = []
    norm = 0
    for i in x:
        for j in i:
            q = j * j
            l.append(q)
    for number in l:
        norm += number
    norma_final = norm**0.5
    return norma_final


def é_simétrica(x: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    if x == []:
        return True
    if len(x) == len(x[0]) and transposta(x) == x:
        return True
    else:
        return False
    # : implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # a transposta de uma matriz é a matriz que tem as linhas da matriz original como colunas e as colunas da matriz original como linhas


def transposta(x: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    transpst = []
    if x == []:
        return []
    for i in range(len(x[0])):
        transpst.append([])
        for j in range(len(x)):
            transpst[i].append(x[j][i])

    return transpst

    #: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]
