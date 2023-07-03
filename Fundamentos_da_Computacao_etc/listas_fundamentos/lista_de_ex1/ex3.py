altura = float(input("Insira a sua altura, use '.' ao invés de vírgula: "))
peso = float(input("Insira o seu peso em kg, use '.' ao invés de virgula: "))
imc = peso/altura**2
print(f"O seu IMC é de {imc:.2f}.")