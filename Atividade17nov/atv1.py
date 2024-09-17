valores = []
quant_impar = 0

for i in range(7):
    valor = int(input(f"Digite o {i+1}° valor: "))
    valores.append(valor)

for valor in valores:
    if valor % 2 != 0:  # Se o valor é ímpar
        quant_impar += 1
print(f"A quantidade de números ímpares na lista é: {quant_impar}")
