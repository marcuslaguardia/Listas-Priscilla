vetor = [0]*15
# vetor_semneg = [0]*15
for i in range(15):
    elem = int(input("Insira um valor para o vetor: "))
    if elem < 0:
        vetor[i] = 0
    else:
        vetor[i] = elem
print(vetor)

