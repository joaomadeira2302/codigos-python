def calcular_multa(velocidade_registrada, limite_velocidade):
    excesso = vel_reg - lim_vel
    
    if excesso > 0:
        if excesso <= 10:
            multa = 50
        elif excesso <= 20:
            multa = 100
        else:
            multa = 200
        print(f"Multa: R$ {multa},00")
    else:
        print("Sem multa")

vel_reg = float(input("Qual foi a velocidade registrada do veículo (em km/h)? "))
lim_vel = float(input("Qual é o limite de velocidade da via (em km/h)? "))

# Chama a função para calcular a multa
calcular_multa(vel_reg, lim_vel)
