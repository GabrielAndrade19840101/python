# 2) Escreva uma programa em Python que recebe duas matrizes como entrada e retorna a multiplicação dessas matrizes.

def multiplicar_matrizes(matrizA, matrizB):
    # Número de linhas da matriz A
    linhasA = len(matrizA)
    # Número de colunas da matriz A / Número de linhas da matriz B
    colunasA = len(matrizA[0])
    # Número de colunas da matriz B
    colunasB = len(matrizB[0])

    # Verifica se a multiplicação é possível
    if colunasA != len(matrizB):
        raise ValueError("Número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B")

    # Cria a matriz resultante
    resultado = [[0 for _ in range(colunasB)] for _ in range(linhasA)]

    # Realiza a multiplicação
    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA):
                resultado[i][j] += matrizA[i][k] * matrizB[k][j]

    return resultado

# Exemplo de uso
matrizA = [[1, 2, 3], [4, 5, 6]]
matrizB = [[7, 8], [9, 10], [11, 12]]

matriz_resultante = multiplicar_matrizes(matrizA, matrizB)
print(matriz_resultante)