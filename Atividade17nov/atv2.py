lista = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}° numero: "))
    lista.append(numero)

for i in range(len(lista)):
    if lista[i] == 10:
        print(f"O valor 10 esta no indice {i}.")

if 10 not in lista:
    print("O valor 10 não está na lista.")