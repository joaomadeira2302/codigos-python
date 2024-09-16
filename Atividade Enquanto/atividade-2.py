cont_impar = 0
while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    if valor % 2 != 0:
        cont_impar += 1
print(f"Quantidade de números ímpares: {cont_impar}")
