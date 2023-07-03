def nome_escada(nome):
    for i in range(len(nome)):
        for j in range(i+1):
            print(nome[j],end = '')
        print()

nome = input("Insira um nome: ")
nome_escada(nome)
