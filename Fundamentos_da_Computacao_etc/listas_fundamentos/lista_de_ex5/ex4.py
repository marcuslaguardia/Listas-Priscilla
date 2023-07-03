def ler_string():
    string = input("Insira uma string: ")
    return string

def contar_espaco_vogal(string):
    cont_espaco = 0
    cont_vogal = 0
    for i in range(len(string)):
        if string[i].lower() == "a" or \
        string[i].lower() == 'e' or \
        string[i].lower() == 'i' or \
        string[i].lower() == 'o' or \
        string[i].lower() == 'u':
            cont_vogal += 1
        elif string[i] == " ":
            cont_espaco += 1

    print(f"Na string {string}, há {cont_vogal} vogal(is) e {cont_espaco} espaço(s) branco(s).")

string = ler_string()
resultado = contar_espaco_vogal(string)
