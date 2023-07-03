# Faça um programa que determine a matriz resultante da soma de duas
# matrizes 3x2

def leitura_matriz1():
    matriz1 = []
    for i in range(3):
        matriz1.append([])
        for j in range(2):
            elem = int(input("Insira um elemento para a primeira matriz: "))
            matriz1[i].append(elem)
    return matriz1

def leitura_matriz2():
    matriz2 = []
    for i in range(3):
        matriz2.append([])
        for j in range(2):
            elem = int(input("Insira um elemento para a segunda matriz: "))
            matriz2[i].append(elem)
    return matriz2

def soma_matrizes(matriz1,matriz2):
    matriz_soma = []
    for i in range(3):
        matriz_soma.append([])
        for j in range(2):
            matriz_soma[i].append(matriz1[i][j] + matriz2[i][j])
    return matriz_soma

matriz1 = leitura_matriz1()
print(matriz1)
matriz2 = leitura_matriz2()
print(matriz2)
soma = soma_matrizes(matriz1,matriz2)