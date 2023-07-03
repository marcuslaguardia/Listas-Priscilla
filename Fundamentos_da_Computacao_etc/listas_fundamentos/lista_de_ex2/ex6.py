n = int(input("Insira um número inteiro positivo: "))
if n < 0:
    print("O número deve ser positivo.") 
elif n == 0:
    print("O fatorial de 0 é 1.")
elif n == 1:
    print("O fatorial de 1 é 1.")
else:
    fatorial = 1
    for i in range(2,n+1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}.")   