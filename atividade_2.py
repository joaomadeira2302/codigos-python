valor = int(input("Informe seu salario: "))

if valor <= 600:
    valorN = valor*1.3
    print(f"Seu novo salario é: {valorN} ")
else:
    print(f"Seu salario ainda é o mesmo: {valor} ")

