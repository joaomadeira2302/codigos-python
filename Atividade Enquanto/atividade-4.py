while True:
    nome = input("Digite seu nome completo: ")
    if len(nome) > 15:
        print(f"Nome válido: {nome}")
        break
    else:
        print("O nome deve ter mais que 15 letras. Tente novamente.")
    