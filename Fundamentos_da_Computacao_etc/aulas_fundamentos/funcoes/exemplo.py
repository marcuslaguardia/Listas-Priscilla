def lerNumero():
    n = int(input("Informe um valor: "))
    return n

def classificaNum(n):
    if n>0:
        return 'P'
    elif n<0:
        return 'N'
    else:
        return 'Z'

def retorna(x,y):
    y += 1
    y += 2
    return x,y

# num = lerNumero()
n1,n2 = retorna(1,3)
print(n1)
print(n2)
