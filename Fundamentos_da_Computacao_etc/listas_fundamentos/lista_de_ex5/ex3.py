def escada_invertida(nome):
    for i in range(len(nome),0,-1):
        for j in range(i):
            print(nome[j],end='')
        print()

nome = input("Insira um nome: ")
escada_invertida(nome)
