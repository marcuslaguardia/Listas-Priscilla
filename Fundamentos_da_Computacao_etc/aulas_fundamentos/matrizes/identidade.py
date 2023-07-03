mat = [[0]*3, [0]*3, [0]*3]
for lin in range(3):
    for col in range(3):
        if lin == col:
            mat[lin].append(1)
        else:
            mat[lin].append(0)
print(mat)
