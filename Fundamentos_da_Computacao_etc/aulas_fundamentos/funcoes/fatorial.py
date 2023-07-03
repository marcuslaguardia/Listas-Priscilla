def calculo_fatorial(n):
    contador = 1
    for i in range(1,n+1):
        contador *= i
    return contador

num = int(input("num: "))
fatorial = calculo_fatorial(num)
print(f"O fatorial de {num} é {fatorial}")
