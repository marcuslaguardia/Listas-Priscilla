vetor1 = []
vetor2 = []

for i in range(10):
    elem = int(input("Insira um elemento para o primeiro vetor: "))
    vetor1.append(elem)

for i in range(10):
    elem = int(input("Insira um elemento para o segundo vetor: "))
    vetor2.append(elem)

vetor_resultante = []

for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])

print("Vetor resultante:", vetor_resultante)
