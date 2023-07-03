# Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma
# dos elementos de cada coluna e a soma dos elementos das diagonais
# principal e secundária são todas iguais. Dada uma matriz quadrada A, 3x3,
# verificar e exibir se A é um quadrado mágico

def leitura_matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            elem = int(input(f"Insira um elemento para [{i}][{j}]: "))
            matriz[i].append(elem)
    return matriz

def verificar_quadrado_magico(matriz):
    # Cálculo da soma esperada
    soma_esperada = 0
    for j in range(3):
        soma_esperada += matriz[0][j]

    # Verificação de soma das linhas
    for i in range(len(matriz)):
        soma_linha = 0
        for j in range(len(matriz[i])):
            soma_linha += matriz[i][j]
        if soma_linha != soma_esperada:
            return False
    
    # Verificação de soma das colunas
    for j in range(3):
        soma_coluna = 0
        for i in range(3):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_esperada:
            return False
    
    # Verificação da soma da diagonal princincipal
    soma_diagonal_principal = 0
    for i in range(3):
        soma_diagonal_principal += matriz[i][i]
    if soma_diagonal_principal != soma_esperada:
        return False
    
    # Verificação da soma da diagonal secundária
    soma_diagonal_secundaria = 0
    for i in range(3):
        soma_diagonal_secundaria += matriz[i][2 - i]
    if soma_diagonal_secundaria != soma_esperada:
        return False

    return True

matriz = leitura_matriz()
if verificar_quadrado_magico(matriz):
    print("A matriz é um quadrado mágico!")
else:
    print("A matriz não é um quadrado mágico.")
