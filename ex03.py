# 3) Escreva uma programa em Python que recebe uma matriz como entrada e retorna a transposta dessa matriz.
def transpor_matriz(matriz):
    # Calcula a transposta usando compreensão de lista
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta

# Exemplo de uso
matriz_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_transposta = transpor_matriz(matriz_original)
print(matriz_transposta)