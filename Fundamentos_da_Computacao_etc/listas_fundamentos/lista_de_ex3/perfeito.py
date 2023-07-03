def verificar_perfeito(numero):
    soma_div = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_div += i

    if soma_div == numero:
        return True
    else:
        return False

# Solicitar ao usuário um número para verificar se é perfeito
numero_usuario = int(input("Digite um número: "))

# Chamar a função para verificar se o número é perfeito
if verificar_perfeito(numero_usuario):
    print(f"{numero_usuario} é perfeito.")
else:
    print(f"{numero_usuario} não é perfeito.")
