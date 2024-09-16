ht = float(input("Insira o número de horas trabalhadas: "))
vph = float(input("Insira o valor por hora: "))

if ht > 40:
    hora_extra = ht - 40
    salario = (40 * vph) + (hora_extra * vph * 1.5)
else:
    salario = ht * vph

print(f"O salário total é: R$ {salario:.2f}")
