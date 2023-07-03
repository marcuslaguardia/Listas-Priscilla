mat1 = [[0]*3,[0]*3,[0]*3]
mat2 = [[0]*3,[0]*3,[0]*3]
mat_soma = [[0]*3,[0]*3,[0]*3]

for lin in range(3):
    for col in range(3):
        mat1[lin][col] = (int(input(f"Insira um elemento para a posição{[lin],[col]}: ")))
print(mat1)

for lin in range(3):
    for col in range(3):
        mat2[lin][col] = (int(input(f"Insira um elemento para a posição {[lin],[col]}: ")))
print(mat2)

for lin in range(3):
    for col in range(3):
        mat_soma[lin][col] = mat1[lin][col] + mat2[lin][col]
print(mat_soma)
