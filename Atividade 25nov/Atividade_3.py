def comparar_idades(idade1, idade2):
    if idade1 > idade2:
        return "A primeira pessoa é mais velha."
    elif idade2 > idade1:
        return "A segunda pessoa é mais velha."
    else:
        return "Ambas as pessoas têm a mesma idade."

def main():
    while True:
        print("\nDigite as idades das duas pessoas (ou 0 para sair):")
        idade1 = int(input("Idade da primeira pessoa: "))
        if idade1 == 0:
            break
        idade2 = int(input("Idade da segunda pessoa: "))
        if idade2 == 0:
            break
        
        resultado = comparar_idades(idade1, idade2)
        print(resultado)

if __name__ == "__main__":
    main()
