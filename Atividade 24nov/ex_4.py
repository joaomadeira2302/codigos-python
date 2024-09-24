import random

def exibir_lista(lista):
    print("Lista de palavras:")
    for i, palavra in enumerate(lista):
        print(f"{i}. {palavra}")

def embaralhar_lista(lista):
    random.shuffle(lista)
    return lista

def escolher_palavra(lista):
    return random.choice(lista)

def jogo():
    palavras = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo']
    

    exibir_lista(palavras)
    
    lista_embaralhada = embaralhar_lista(palavras.copy())
    

    palavra_escolhida = escolher_palavra(lista_embaralhada)
    
    print("\nA lista foi embaralhada e não será mais mostrada.")
    print(f"A palavra escolhida é: {palavra_escolhida}")
    print("A lista começa com a posição 0 e vai até 14.")
    
    tentativas = 3
    while tentativas > 0:
        try:
            posicao = int(input("Em qual posição está essa palavra? "))
            if lista_embaralhada[posicao] == palavra_escolhida:
                print("Parabéns! Você acertou!")
                break
            else:
                tentativas -= 1
                print(f"Você errou. Tentativas restantes: {tentativas}")
        except (ValueError, IndexError):
            print("Entrada inválida. Por favor, digite um número entre 0 e 14.")
    
    if tentativas == 0:
        posicao_correta = lista_embaralhada.index(palavra_escolhida)
        print(f"Você não acertou. A posição correta era: {posicao_correta}")
    
    print("\nLista embaralhada:")
    exibir_lista(lista_embaralhada)

if __name__ == "__main__":
    jogo()