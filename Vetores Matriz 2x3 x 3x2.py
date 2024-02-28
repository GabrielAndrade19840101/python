
def criar_matriz(n_linhas, n_colunas, mensagem):
    """Cria uma matriz com base nos valores fornecidos pelo usuário."""
    print(mensagem)
    matriz = []
    for i in range(n_linhas):
        linha = []  # Cria uma nova linha
        for j in range(n_colunas):
            valor = float(input(f"Entre com o valor para o elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(A, B):
    """Multiplica duas matrizes A e B."""
    n_linhas_A, n_colunas_A = len(A), len(A[0])
    n_linhas_B, n_colunas_B = len(B), len(B[0])
    
    if n_colunas_A != n_linhas_B:
        raise ValueError("As dimensões das matrizes são incompatíveis para multiplicação.")
    
    resultado = [[0 for _ in range(n_colunas_B)] for _ in range(n_linhas_A)]
    for i in range(n_linhas_A):
        for j in range(n_colunas_B):
            for k in range(n_colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

# Solicita ao usuário para criar as matrizes
A = criar_matriz(3, 2, "Insira os valores para a Matriz A (3x2):")
B = criar_matriz(2, 3, "Insira os valores para a Matriz B (2x3):")

# Multiplica as matrizes
resultado = multiplicar_matrizes(A, B)

# Exibe o resultado
print("Matriz Resultante da Multiplicação:")
for linha in resultado:
    print(linha)


