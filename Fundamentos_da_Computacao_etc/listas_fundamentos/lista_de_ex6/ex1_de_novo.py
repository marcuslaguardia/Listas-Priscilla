def ler_matriz():
    matriz = []
    for linha in range(3):
        matriz.append([])
        for coluna in range(3):
            elem = int(input("Insira um elemento: "))
            matriz[linha].append(elem)
    return matriz

def soma_elementos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma

matriz = ler_matriz()
print(matriz)
total = soma_elementos(matriz)
print(f"A soma dos elementos da matriz é {total}")

