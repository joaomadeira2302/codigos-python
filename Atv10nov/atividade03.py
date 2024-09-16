idade = int(input("Insira sua idade: "))

if idade < 12:
    print("Criança")
elif 12 <= idade <= 18:
    print("Adolescente")
elif 19 <= idade <= 60:
    print("Adulto")
else:
    print("Idoso")
