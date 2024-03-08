# 1) Escreva uma programa em Python que recebe dois vetores como entrada e retorna a soma desses vetores.
def soma_vetores(vetor1, vetor2):
    # Verifica se os vetores têm o mesmo tamanho
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")

    # Soma os elementos correspondentes de cada vetor
    vetor_soma = [v1 + v2 for v1, v2 in zip(vetor1, vetor2)]
    return vetor_soma

# Exemplo de uso
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

vetor_resultante = soma_vetores(vetor1, vetor2)
print(vetor_resultante)