num_notas = 20
notas = []
arqnotas = open("ex5.txt", "w")

for i in range(num_notas):
    nota = int(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)
    arqnotas.write(f"{nota}\n")

arqnotas.close()

medianotas = 0
for nota in notas:
    medianotas += nota
medianotas = medianotas / len(notas)

arqnotas = open("ex5.txt", "r")

notasacimamedia = 0
for notaarq in arqnotas.readlines():
    if int(notaarq) > medianotas:
        notasacimamedia +=1


print(f"Existem {notasacimamedia} notas acima da média.")