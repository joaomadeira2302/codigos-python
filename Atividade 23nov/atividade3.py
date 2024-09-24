def main():
    salario_atual = float(input("Digite o salário atual: "))
    anos_servico = int(input("Digite o número de anos de serviço: "))

    if anos_servico <= 5:
        bonificacao_porcentagem = 0.05
    elif 6 <= anos_servico <= 10:
        bonificacao_porcentagem = 0.10
    else:
        bonificacao_porcentagem = 0.15

    bonificacao = salario_atual * bonificacao_porcentagem
    salario_final = salario_atual + bonificacao

    print(f"Valor do bônus: R${bonificacao:.2f}")
    print(f"Salário final com o bônus incluído: R${salario_final:.2f}")


if __name__ == "__main__":
    main()
