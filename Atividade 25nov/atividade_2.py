def adicionar_aluno(notas):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    notas[nome] = nota
    print(f'Aluno {nome} com nota {nota} adicionado.')

def calcular_media(notas):
    if notas:
        media = sum(notas.values()) / len(notas)
        return media
    else:
        return 0

def exibir_acima_da_media(notas, media):
    print(f"\nMédia da turma: {media:.2f}")
    print("Alunos com notas acima da média:")
    for nome, nota in notas.items():
        if nota > media:
            print(f'{nome}: {nota}')

def main():
    notas = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar novo aluno e nota")
        print("2. Calcular média da turma e exibir alunos acima da média")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_aluno(notas)
        elif opcao == '2':
            media = calcular_media(notas)
            exibir_acima_da_media(notas, media)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
