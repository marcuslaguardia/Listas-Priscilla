vetpos = [0] * 10
vetneg = [0] * 10
for i in range(10):
    elem = int(input("Insira um valor: "))
    if elem > 0:
        vetpos[i] = elem
    else:
        vetneg[i] = elem

print(vetpos)
print(vetneg)
