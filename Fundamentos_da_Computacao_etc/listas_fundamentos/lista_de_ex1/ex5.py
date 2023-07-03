a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    # Os valores formam um triângulo
    perimetro = a + b + c
    print("Os valores formam um triângulo.")
    print(f"O perímetro do triângulo é {perimetro}.")
else:
    # Os valores não formam um triângulo
    print("Os valores não formam um triângulo.")
