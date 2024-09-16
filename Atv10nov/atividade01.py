num = int(input("Insira um número entre 0 e 100: "))

if 0 <= num <= 25:
    print("O número está entre 0 a 25.")
elif 26 <= num <= 50:
    print("O número está entre 26 a 50.")
elif 51 <= num <= 75:
    print("O número está entre 51 a 75.")
elif 76 <= num <= 100:
    print("O número está entre 76 a 100.")
else:
    print("Número fora da faixa permitida.")