
lista1 = [1, 2, 3, 4, 5]  
lista2 = [6, 7, 8, 9, 10]  
resultado = [0] * 5        

for i in range(5):
    resultado[i] = lista1[i] + lista2[i]

print("A soma dos elementos das duas listas é:")
for i in range(5):
    print(resultado[i])
