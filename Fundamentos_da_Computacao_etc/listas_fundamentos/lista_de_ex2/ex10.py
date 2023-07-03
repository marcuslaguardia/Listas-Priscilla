numero = int(input("Insira um número: "))

if numero == 1:
    print(f"{numero} não é primo.")
else:
    primo = True
    div = 2

    while div*div <= numero:
        if numero % div == 0:
            primo = False
            break
        div += 1

    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")