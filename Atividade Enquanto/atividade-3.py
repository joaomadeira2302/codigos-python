# Inicializando variáveis
soma_positivos = 0
quantidade_negativos = 0
contador = 0

# Loop que será executado 10 vezes
while contador < 10:
    valor = int(input("Digite um valor inteiro: "))
    
    # Se o valor for positivo, adiciona à soma dos positivos
    if valor > 0:
        soma_positivos += valor
    # Se o valor for negativo, incrementa o contador de negativos
    elif valor < 0:
        quantidade_negativos += 1
    
    # Incrementa o contador para controlar as 10 iterações
    contador += 1

# Exibindo os resultados
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")
