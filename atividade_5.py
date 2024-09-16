percurso = int(input("Percurso em km: "))
carro = int(input("Qual o carro? Digite 1, 2 ou 3: "))

if carro == 1:
    valorR1 = percurso/8
    print(f"O consulmo será: {valorR1:.2f}litros")

if carro == 2:
    valorR2 = percurso/9
    print(f"O consulmo será: {valorR2:.2f}litros")

if carro == 3:
    valorR3 = percurso/12
    print(f"O consulmo será: {valorR3:.2f}litros")