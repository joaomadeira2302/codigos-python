def exibir_eventos(eventos):
    if not eventos:
        print("Nenhum evento agendado.")
    else:
        print("Eventos agendados:")
        for i, evento in enumerate(eventos, start=1):
            print(f"{i}. {evento}")

def adicionar_evento(eventos):
    novo_evento = input("Digite o novo evento: ")
    eventos.append(novo_evento)
    print(f"Evento '{novo_evento}' adicionado com sucesso!")

def remove_event(eventos):
    exibir_eventos(eventos)
    if eventos:
        try:
            indice = int(input("Digite o número do evento que deseja remover: "))
            if 1 <= indice <= len(eventos):
                evento_removido = eventos.pop(indice - 1)
                print(f"Evento '{evento_removido}' removido com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

eventos = []

while True:
    print("\nMenu:")
    print("1. Exibir eventos")
    print("2. Adicionar evento")
    print("3. Remover evento")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        exibir_eventos(eventos)
    elif opcao == '2':
        adicionar_evento(eventos)
    elif opcao == '3':
        remove_event(eventos)
    elif opcao == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
