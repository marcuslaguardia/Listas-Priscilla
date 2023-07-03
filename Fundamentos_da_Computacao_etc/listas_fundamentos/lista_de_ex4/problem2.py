vetor = [0] * 10
vetor_inverso = [0] * 10
for i in range(10):
    elem = int(input("Insira um elemento: "))
    vetor[i] = elem
print(f"Vetor antes da inversao: {vetor}")

for i in range(10):
    vetor_inverso[i] = vetor[len(vetor)-i-1]
print(f"Vetor apos a inversao: {vetor_inverso}")
