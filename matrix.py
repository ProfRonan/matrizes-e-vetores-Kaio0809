"""Módulo com as funções de manipulação de matrizes."""


def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """Soma duas matrizes"""
    if(len(x) != len(y) or len(x[0]) != len(y[0])):
        return None
    result = []
    for i in range(len(x)):   
        result.append([])
        for j in range(len(x[0])):
            result[i].append(x[i[j]] + y[i[j]])
    return result



def multiplicação_por_escalar(matriz: list[list[float]], escalar: float) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    result =[]
    for line in matriz:
        newLine = []
        for element in line:
            newLine.append(element * escalar)

        result.append(newLine)

    return result


def multiplicação(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """Multiplica duas matrizes"""
    if x == []:
        return x 
    if len(x) != len(y[0]):
        return None
        
    else:
        rowsx = len(x)
        cols_x = len(x[0])
        cols_y = len(y[0])
        C = [[0 for _ in range(cols_y)] for _ in range(cols_x)]
        for i in range(rowsx):
            for j in range(cols_y):
                for k in range(cols_x):
                    C[i][j] += x[i][k] * y[k][j]
        return C



def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    l = []
    norm = 0
    for i in x:
        for j in i:
            q = j**2
            l.append(q)
        for number in l:
            norm += number
    norma_final = norm**0.5
    return norma_final


def é_simétrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    # uma matriz é simétrica se ela é quadrada e se ela é igual a sua transposta
    # a transposta de uma matriz é a matriz que tem as linhas da matriz original como colunas e as colunas da matriz original como linhas


def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    # TODO: implementar
    # a transposta de uma matriz [[1, 2, 4], [2, 3, 4]] é [[1, 2], [2, 3], [4, 4]]
