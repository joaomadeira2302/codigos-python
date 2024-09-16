# Inicializando a contagem de números ímpares
contagem_impares = 0

while True:
    # Solicitando um valor numérico do usuário
    numero = int(input("Digite um valor (0 para sair): "))
    
    # Verificando se o valor é 0 para encerrar o loop
    if numero == 0:
        break
    
    # Verificando se o número é ímpar
    if numero % 2 != 0:
        contagem_impares += 1

# Exibindo a quantidade de números ímpares digitados
print(f"Quantidade de números ímpares: {contagem_impares}")
