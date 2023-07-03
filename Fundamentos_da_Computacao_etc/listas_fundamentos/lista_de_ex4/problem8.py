vetor = []

for i in range(10):
    elem = int(input("Insira um número para o vetor: "))
    vetor.append(elem)

x = int(input("Insira um número x: "))

multiplos = []
quantidade = 0

for num in vetor:
    if num % x == 0:
        quantidade += 1
        multiplos.append(num)

print(f"A quantidade de múltiplos de {x} no vetor é: {quantidade}")
print("Os múltiplos são: ", end="")
for num in multiplos:
    print(num, end=" ")
