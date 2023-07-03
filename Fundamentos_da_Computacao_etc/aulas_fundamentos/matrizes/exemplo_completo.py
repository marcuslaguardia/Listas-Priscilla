linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
mat = []

for lin in range(linhas):
    mat.append([])
    for col in range(colunas):
        mat[lin].append(int(input(f'Valor de {[lin][col]}: ')))
print(mat)
