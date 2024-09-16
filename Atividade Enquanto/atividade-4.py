# Loop que continuará pedindo o nome até que tenha mais de 15 letras
while True:
    nome = input("Digite seu nome completo: ")
    
    # Verifica se o nome tem mais de 15 letras
    if len(nome) > 15:
        print(f"Nome válido: {nome}")
        break  # Sai do loop se o nome tiver mais de 15 letras
    else:
        print("O nome deve ter mais de 15 letras. Tente novamente.")
