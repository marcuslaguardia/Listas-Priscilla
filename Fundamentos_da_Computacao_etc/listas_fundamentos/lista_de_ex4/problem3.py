vetor = [0] * 10
for i in range(10):
    elem = int(input("Insira um elemento para o vetor: "))
    if elem % 2 != 0:
        vetor[i] = elem
print(vetor)
