vetor = [0] * 15
for i in range(15):
    elem = int(input("Insira um elemento para o vetor > "))
    vetor[i] = elem
print(vetor)

maior_elemento = vetor[0]
menor_elemento = vetor[0]
pos_maior = 0
pos_menor = 0

for i in range(1, 15):
    if vetor[i] > maior_elemento:
        maior_elemento = vetor[i]
        pos_maior = i
    elif vetor[i] < menor_elemento:
        menor_elemento = vetor[i]
        pos_menor = i

diferenca = maior_elemento - menor_elemento
print(f"O maior elemento no vetor é {maior_elemento} e ocupa a posição {pos_maior}.")
print(f"O menor elemento no vetor é {menor_elemento} e ocupa a posição {pos_menor}.")
print(f"A diferença entre o maior e o menor é {diferenca}.")
