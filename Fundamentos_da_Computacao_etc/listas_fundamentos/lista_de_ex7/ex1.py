nome_arq = "olamundo.txt"

arq = open("olamundo.txt", "w")
arq.write("Olá mundo")
arq.close()

arq = open(nome_arq, "r")
linhas = arq.readlines()
total_linhas = len(linhas)
arq.close()

print(f"O arquivo possui {total_linhas} linhas.")