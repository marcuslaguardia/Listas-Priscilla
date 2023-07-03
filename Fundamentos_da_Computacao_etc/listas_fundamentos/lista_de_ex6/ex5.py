# Construa um programa que calcule e armazene em um vetor o maior
# elemento de cada linha de uma matriz 3x3.

def leitura_matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            elem = int(input("Insira um elemento: "))
            matriz[i].append(elem)
    return matriz

def achar_maior_numero(matriz):
    vetor_maior_elemento = []
    for linha in range(len(matriz)):
        maior = matriz[linha][0]
        for i in range(1, len(matriz[linha])):
            if matriz[linha][i] > maior:
                maior = matriz[linha][i]
        vetor_maior_elemento.append(maior)
    return vetor_maior_elemento

matriz = leitura_matriz()
print(matriz)
maior_elemento = achar_maior_numero(matriz)
print(f"O maior elemento da matriz é {maior_elemento}")