def ler_notas():
    notas = []
    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def contar_acima_da_media(notas, media):
    return sum(1 for nota in notas if nota > media)

notas = ler_notas()

media = calcular_media(notas)

acima_da_media = contar_acima_da_media(notas, 7)


print(f"A quantidade de alunos com notas acima da média (7) é: {acima_da_media}")
