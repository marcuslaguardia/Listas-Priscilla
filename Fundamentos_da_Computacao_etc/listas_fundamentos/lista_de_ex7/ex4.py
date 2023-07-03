primeiro_arquivo = open("texto1.txt","w")
primeiro_arquivo.write("Olá ")
primeiro_arquivo.close()

segundo_arquivo = open("texto2.txt","w")
segundo_arquivo.write("Mundo!")
segundo_arquivo.close()

primeiro_arquivo = open("texto1.txt","r")
segundo_arquivo = open("texto2.txt","r")

terceiro_arquivo = open("ex4.txt","w")

texto_atual = primeiro_arquivo.readline()
while len(texto_atual) != 0:
    terceiro_arquivo.write(texto_atual)
    texto_atual = primeiro_arquivo.readline()

texto_atual = segundo_arquivo.readline()
while len(texto_atual) != 0:
    terceiro_arquivo.write(texto_atual)
    texto_atual = segundo_arquivo.readline()

terceiro_arquivo.write("\n")
primeiro_arquivo.close()
segundo_arquivo.close()
terceiro_arquivo.close()

terceiro_arquivo = open("ex4.txt","r")

for i in terceiro_arquivo.readlines():
    print(i[:-1])
