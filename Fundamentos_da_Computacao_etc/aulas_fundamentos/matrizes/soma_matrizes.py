mat1 = [[0]*3,[0]*3,[0]*3]
mat2 = [[0]*3,[0]*3,[0]*3]
mat_soma = [[0]*3,[0]*3,[0]*3]

for lin in range(3):
    for col in range(3):
        mat1[lin][col] = (int(input("Insira um elemento: ")))
print(mat1)

for lin in range(3):
    for col in range(3):
        mat2[lin][col] = (int(input("Insira um elemento: ")))
print(mat2)

for lin in range(3):
    for col in range(3):
        mat_soma[lin][col] = mat1[lin][col] + mat2[lin][col]
print(mat_soma)
