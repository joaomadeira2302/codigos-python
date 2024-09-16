soma = 0
cont = 0
for num in range(51, 71):
    if num % 2 == 0:
        soma += num
        cont = cont + 1
med = soma / cont
print(f"Soma dos valores pares: {soma}")
print(f"Média aritmética dos valores pares: {med}")