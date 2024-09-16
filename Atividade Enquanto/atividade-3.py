somaP = 0
quantN = 0
contador = 0
while contador < 10:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        somaP += valor
    elif valor < 0:
        quantN += 1
    contador += 1
print(f"Soma dos números positivos: {somaP}")
print(f"Quantidade de números negativos: {quantN}")