# 4) Escreva uma programa em Python que reba uma matriz quadrada e calcule a matriz inversa.

import numpy as np

def calcular_inversa(matriz):
    matriz_np = np.array(matriz)
    try:
        inversa = np.linalg.inv(matriz_np)
    except np.linalg.LinAlgError:
        # A inversa não existe se a matriz é singular (determinante é zero)
        return None
    return inversa

# Exemplo de uso
matriz_quadrada = [[1, 2], [3, 4]]

matriz_inversa = calcular_inversa(matriz_quadrada)
if matriz_inversa is not None:
    print(matriz_inversa)
else:
    print("A matriz não tem inversa.")