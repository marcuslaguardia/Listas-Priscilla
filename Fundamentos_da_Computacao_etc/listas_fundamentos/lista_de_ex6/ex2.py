# Escreva um programa que leia uma matriz 3x3 e armazene em um vetor a
# soma dos elementos por linha.

def leitura_matriz3x3():
    matriz3x3 = []
    for i in range(3):
        matriz3x3.append([])
        for j in range(3):
            elem = int(input("Insira um elemento: "))
            matriz3x3[i].append(elem)
    return matriz3x3

def soma_1coluna(matriz3x3):
    vetor_soma = []
    for i in range(len(matriz3x3)):
        soma = 0
        for j in range(len(matriz3x3[i])):
            soma += matriz3x3[i][j]
        vetor_soma.append(soma)
    return vetor_soma

def vetor_novo(matriz3x3):
    vetor_soma_colunas = soma_1coluna(matriz3x3)
    matriz_soma_colunas = []
    for j in range(len(vetor_soma_colunas)):
        matriz_soma_colunas.append([vetor_soma_colunas[j]])
    return matriz_soma_colunas

matriz3x3 = leitura_matriz3x3()
print(matriz3x3)
novo_vetor = vetor_novo(matriz3x3)
print(novo_vetor)


