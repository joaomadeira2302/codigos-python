import random

opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

E_comput = random.randint(1, 3)

E_user = int(input("Escolha uma opção (1 - Pedra, 2 - Papel, 3 - Tesoura): "))

if E_user == E_comput:
    print("Empate!")
elif (E_user == 1 and E_comput == 3) or (E_user == 2 and E_comput == 1) or (E_user == 3 and E_comput == 2):
    print(f"Você escolheu {opcoes[E_user]} e o computador escolheu {opcoes[E_comput]}. Você ganhou!")
else:
    print(f"Você escolheu {opcoes[E_user]} e o computador escolheu {opcoes[E_comput]}. O computador ganhou!")

