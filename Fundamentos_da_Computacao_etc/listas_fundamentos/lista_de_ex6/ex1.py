# Faça um programa que leia uma matriz 3x3 e ao final imprima a soma de seus
# elementos.

def ler_matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            elem = int(input("Insira um elemento: "))
            matriz[i].append(elem)
    return matriz
def soma_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma 

matriz = ler_matriz()
print(matriz)
total = soma_matriz(matriz)
print(f"A soma dos elementos da matriz é {total}")
