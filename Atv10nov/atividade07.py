nota_final = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (%): "))


if nota_final >= 7 and frequencia >= 75:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
