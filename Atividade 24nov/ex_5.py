import random

moeda = ["Cara", "Coroa"]

resultados = []

while True:
    
    resultado = random.choice(moeda)
    print(f"Resultado do lançamento: {resultado}")
    
    
    resultados.append(resultado)
    
    repetir = input("Deseja lançar a moeda novamente? (s/n): ").strip().lower()
    if repetir != 's':
        break

print("Resultados dos lançamentos:", resultados)
