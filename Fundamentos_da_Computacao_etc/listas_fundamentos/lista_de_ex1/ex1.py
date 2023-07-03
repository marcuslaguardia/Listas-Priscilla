a = int(input("Insira o valor da primeira varíavel: "))
b = int(input("Insira o valor da segunda variável: "))
print(f"Os valores anteriores à troca são: A = {a} e B = {b}.")

aux = a
a = b
b = aux
print(f"Após a troca de valores, o valor de A é {a} e o valor de B é {b}")