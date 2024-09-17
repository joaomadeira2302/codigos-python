
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp = [0] * 12  

for i in range(12):
    temp[i] = float(input(f"Digite a temperatura media de {meses[i]}: "))

soma_temp = 0
for i in range(12):
    soma_temp += temp[i]
media_anual = soma_temp / 12

print(f"\nA media anual de temperatura foi: {media_anual:.2f}°C\n")

print("Meses com temperatura acima da media anual:")
for i in range(12):
    if temp[i] > media_anual:
        print(f"{i+1} - {meses[i]}: {temp[i]:.2f}°C")
