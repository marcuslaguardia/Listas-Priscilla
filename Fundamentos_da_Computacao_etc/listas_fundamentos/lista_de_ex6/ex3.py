# Construa um programa que leia uma matriz 4x4 e calcule e imprima a soma
# da diagonal principal.

def leitura_matriz4x4():
    matriz4x4 = []
    for i in range(4):
        matriz4x4.append([])
        for j in range(4):
            elem = int(input("Insira um elemento: "))
            matriz4x4[i].append(elem)
    return matriz4x4

def soma_diagonal_principal(matriz4x4):
    soma = 0
    for i in range(len(matriz4x4)):
        soma += matriz4x4[i][i]
    return soma

matriz = leitura_matriz4x4()
print(matriz)
soma = soma_diagonal_principal(matriz)
print(f"A soma da diagonal principal da matriz é {soma}")