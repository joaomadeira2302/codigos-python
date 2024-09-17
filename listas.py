animais = ['Cachorro','Gato','Ovelha']
print(type(animais)) #exibindo o tipo da variael 

print(animais)

print('-'*50)
# Estamos exibindo todos os itens da lista 'animais'
for elementos in animais:
    print(elementos)

# 1ª etapa: Atualização de dados
print('-'*50)
animais[0] = "Coelho" 
print(animais)

# 2ª etapa: Inserir itens na lista
print('-'*50)
# Forma 1, usando append 
animais.append("Cavalo") # Irá inserir um novo item no final da lista
print(animais)

# Forma 2 - usando insert
animais.insert(1,"Girafa") #O insert precisa de dois valores, o primeiro é a posição onde será inserido, e o seundo é o conteúdo que será inserido na lista.
print(animais)

#3ª etapa: Ecluir itens na lista
print('-'*50)

# Forma 1 - usando pop()
animais.pop() # Irá excluir sempre o ultimo item
print(animais)

# Forma 2 - usando pop() com indice
animais.pop(0) # Aqui escolhemos qual indice da lista será excçuido
print(animais)

# Forma 3 - usando remove
animais.remove("Ovelha") #Irá remover o item pelo seu conteúdo
print(animais)
