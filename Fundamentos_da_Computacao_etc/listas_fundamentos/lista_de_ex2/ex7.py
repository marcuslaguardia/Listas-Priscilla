n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

escolha = 0

while escolha != 5:
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Subtrair
    [ 4 ] Dividir
    [ 5 ] Sair
    """)

    escolha = int(input("O que gostaria de fazer? "))

    if escolha == 1:
        print(f"Resultado da soma entre {n1} e {n2}: {n1 + n2}")
    elif escolha == 2:
        print(f"Resultado da multiplicação entre {n1} e {n2}: {n1 * n2}")
    elif escolha == 3:
        print(f"Resultado da subtração entre {n1} e {n2}: {n1 - n2}")
    elif escolha == 4:
        print(f"O resultado da divisão entre {n1} e {n2}: {n1 / n2}")
    elif escolha == 5:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")
