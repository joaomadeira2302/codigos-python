altura = float(input("Informe sua altura: "))
sexo = int(input("Você é digite 1(homem) ou 2(mulher): "))

if  sexo == 1:
    peso = (72.7 * altura) - 58
    print(f"peso ideal: {peso:.2f}kg")
else:
    peso = (62.1 * altura) - 44.7
    print(f"peso ideal: {peso:.2f}kg")
