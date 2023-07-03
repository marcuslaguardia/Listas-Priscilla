soma = 0
for i in range(85,907+1):
    if i % 2 == 0:
        print(f"{i} é par.")
        soma += i
print(f"A soma dos valores é {soma}.")