valor = int(input("Informe um valor numérico: "))

if valor >= 50:
    print(f"O número {valor} é maior ou igual a 50")
#elif é o mesmo else if, junção dos dois   
elif valor > 30 and valor < 50:
     print(f"O número {valor} está entre 30 e 50")

else:
     print(f"O número {valor} é menos que 30\n") 