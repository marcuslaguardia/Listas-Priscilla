numero_inteiros_vetor = 20

def ler_vetor():
    global numero_inteiros_vetor
    vetor = []
    for i in range(numero_inteiros_vetor):
        vetor.append(int(input(f"Escreva um valor ({i+1} de {numero_inteiros_vetor}): ")))
    return vetor

def ler_arquivo_vetor(arquivo):
    vetor_n = []
    valores = arquivo.readlines()
    for v in valores:
        if v != "":
            vetor_n.append(int(v))
    return vetor_n

def guarde_o_vetor(arquivo, vet):
    for i in vet:
        arquivo.write(f"{i}\n")

arquivo = open("exercicio3.txt", "w")

vet1 = ler_vetor()
guarde_o_vetor(arquivo, vet1)
arquivo.close()

arquivo = open("exercicio3.txt", "r")
vet2 = ler_arquivo_vetor(arquivo)
arquivo.close()

for i in range(len(vet1)):
    print(f"{vet1[i]} | {vet2[i]}")
