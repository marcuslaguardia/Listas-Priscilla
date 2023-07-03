def conta_espaco_vogal(cadeia):
    cont_esp = 0
    cont_vogal = 0
    for i in range(len(cadeia)):
        if cadeia[i].upper() in ["A", "E", "I", "O", "U"]:
            cont_vogal += 1
        elif cadeia[i] == " ":
            cont_esp += 1

    print(f"Na string '{cadeia}', as vogais 'a', 'e', 'i', 'o' e 'u' apareceram {cont_vogal} vezes.")
    print(f"Além disso, espaços em branco apareceram {cont_esp} vezes.")


cadeia = input("Insira uma cadeia: ")
conta_espaco_vogal(cadeia)
