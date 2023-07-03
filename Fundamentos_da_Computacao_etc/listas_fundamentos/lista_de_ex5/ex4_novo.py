def contador_espaco_vogal(cadeia):
    cont_esp = 0
    cont_vogal = 0
    vogais = ["A", "E", "I", "O", "U"]
    for i in range(len(cadeia)):
        if cadeia[i].upper() == "A" or cadeia[i].upper() == "E" or cadeia[i].upper() == "I" or cadeia[i].upper() == "O" or cadeia[i].upper() == "U":
            cont_vogal += 1
        elif cadeia[i] == " ":
            cont_esp += 1

    print(f"Na string '{cadeia}', as vogais 'a', 'e', 'i', 'o' e 'u' apareceram {cont_vogal} vezes.")
    print(f"Além disso, espaços em branco apareceram {cont_esp} vezes.")

cadeia = input("Insira uma cadeia: ")
contador_espaco_vogal(cadeia)

