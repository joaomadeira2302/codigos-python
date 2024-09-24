import time

seg = int(input("Digite o número de segundos que você deseja contar: "))

contador = 0

while contador <= seg:
    print(contador)
    time.sleep(1)
    contador += 1