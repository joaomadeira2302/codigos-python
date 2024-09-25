def calcular_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return valor_final

def main():
    resultados = []
    for _ in range(5):
        valor = float(input("Digite o valor do produto: "))
        percentual = float(input("Digite o percentual de desconto: "))
        valor_com_desconto = calcular_desconto(valor, percentual)
        resultados.append(valor_com_desconto)
        print(f"Valor final com desconto: R${valor_com_desconto:.2f}")

    print("\nLista de valores finais com desconto:")
    for i, valor in enumerate(resultados, 1):
        print(f"{i}. R${valor:.2f}")

if __name__ == "__main__":
    main()
