x = int(input("Insira o valor da base da potenciação: "))
while x < 2:
    x = int(input("Insira o valor da base da potenciação: "))
n = int(input("Insira o valor do expoente: "))
while n < 1:
    n = int(input("Insira o valor do expoente: "))
potencia = x**n
print(f"{x} elevado a {n} é igual a {potencia}.")