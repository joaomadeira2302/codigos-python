def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar novo livro")
    print("2. Remover um livro")
    print("3. Exibir catálogo completo")
    print("4. Sair")

def adicionar_livro(catalogo):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    catalogo[titulo] = autor
    print(f'Livro "{titulo}" de {autor} adicionado ao catálogo.')

def remover_livro(catalogo):
    titulo = input("Digite o título do livro a ser removido: ")
    if titulo in catalogo:
        del catalogo[titulo]
        print(f'Livro "{titulo}" removido do catálogo.')
    else:
        print(f'Livro "{titulo}" não encontrado no catálogo.')

def exibir_catalogo(catalogo):
    if catalogo:
        print("\nCatálogo de Livros:")
        for titulo, autor in catalogo.items():
            print(f'Título: {titulo}, Autor: {autor}')
        print(f'\nTotal de livros no catálogo: {len(catalogo)}')
    else:
        print("\nO catálogo está vazio.")

def main():
    catalogo = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_livro(catalogo)
        elif opcao == '2':
            remover_livro(catalogo)
        elif opcao == '3':
            exibir_catalogo(catalogo)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
