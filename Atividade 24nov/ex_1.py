def ler_lista():
    return list(map(int, input("Digite os números da lista separados por espaço: ").split()))

def encontrar_intersecao(lista1, lista2):
    return sorted(list(set(lista1) & set(lista2)))

# Ler as duas listas do usuário
print("Digite os números para a primeira lista:")
lista1 = ler_lista()
print("Digite os números para a segunda lista:")
lista2 = ler_lista()

# Encontrar a interseção e exibir o resultado
intersecao = encontrar_intersecao(lista1, lista2)
print("Números comuns em ambas as listas, em ordem crescente:", intersecao)
