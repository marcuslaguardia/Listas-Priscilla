def leitura_matriz4x4():
    matriz4x4 = []
    for i in range(4):
        matriz4x4.append([])
        for j in range(4):
            elem = int(input("Insira um elemento: "))
            matriz4x4[i].append(elem)
    return matriz4x4

def maior_elemento_diagonal_principal(matriz):
    maior = matriz[0][0]
    for i in range(1, 4):
        if matriz[i][i] > maior:
            maior = matriz[i][i]
    return maior

def soma_diagonal_secundaria(matriz4x4):
    soma_diag_sec = 0
    tam = len(matriz4x4)
    for i in range(tam):
        soma_diag_sec += matriz4x4[i][tam-i-1]
    return soma_diag_sec

matriz = leitura_matriz4x4()
maior_diag_prin = maior_elemento_diagonal_principal(matriz)
diag_sec = soma_diagonal_secundaria(matriz)
print(matriz)
print(f"O maior elemento da diagonal principal é {maior_diag_prin}.")
print(f"A soma dos elementos da diagonal secundária é {diag_sec}.")