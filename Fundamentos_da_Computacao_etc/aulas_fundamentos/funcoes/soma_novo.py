def lerNumero():
    n = int(input("Informe um valor: "))
    return n

def soma(x,y):
    resultado = x + y
    return resultado

n1 = lerNumero()
n2 = lerNumero()
total = soma(n1,n2)
print(f"Soma: {total}")
