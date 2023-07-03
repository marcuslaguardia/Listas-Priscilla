cont = 0

arquivo_texto = "arquivo.txt"

arquivo = open("arquivo.txt","w")
arquivo.write("The quick brown fox jumps over the lazy dog")
arquivo.close()

arquivo = open(arquivo_texto,"r")
linha = arquivo.readline()
vogais = ["a","e","i","o","u"]

while linha:
    for caracter in linha:
        for vogal in vogais:
            if caracter.lower() == vogal:
                cont += 1
    linha = arquivo.readline()
arquivo.close()

print(f"O arquivo tem {cont} vogais.")