def verifica_palindromo(cadeia):
    palindromo = True
    for i in range(0,len(cadeia)):
        if cadeia[i] != cadeia[len(cadeia)-i-1]:
            palindromo = False
    if palindromo:
            print(f"A cadeia {cadeia} é palíndromo.")
    if not palindromo:
            print(f"A cadeia {cadeia} não é palíndromo.")

cadeia = input("Insira uma cadeia: ")
verifica_palindromo(cadeia)
