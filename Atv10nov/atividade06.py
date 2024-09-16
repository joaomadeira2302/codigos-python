
valor_compra = float(input("Digite o valor da compra: "))
quant_parcelas = int(input("Digite a quantidade de parcelas (1 a 24): "))


if 1 <= quant_parcelas <= 24:
    
    if quant_parcelas > 12:
        valor_total = valor_compra * (1 + 0.015) ** (quant_parcelas - 12)
    else:
        valor_total = valor_compra
    valor_parcela = valor_total / quant_parcelas
    
    
    print(f"Valor total a ser pago: R$ {valor_total:.2f}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
else:
    print("Número de parcelas inválido.")
