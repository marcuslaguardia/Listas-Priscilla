vet1 = [0]*10
vet2 = [0]*10
vet_intersec = [0]*10

for i in range(10):
    elem = int(input("Insira um elemento para o primeiro vetor: "))
    vet1[i] = elem
print(vet1)

for j in range(10):
    elem2 = int(input("Insira um elemento para o segundo vetor: "))
    vet2[i] = elem2
print(vet2)

for k in range(10):
    for l in range(10):
        if vet1[k] == vet2[l]:
            vet_intersec[k] = vet1[k]

print(vet_intersec)