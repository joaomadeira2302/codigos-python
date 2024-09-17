#Trabalho com Tuplas

objetos = ('Lápis','Borracha','Caderno')

print(type(objetos)) # A função type() irá exibir o tipo da variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1]) # Estamos apenas exibindo o item, que está na posição 1 

# Exbindo todos os dados a tupla
print('-'*50)

for item in range(0,3):
    print(objetos[item])

# Exibindo todos os dados sem a função range
print('-'*50)

for item in objetos:
    print(item)

#Tentando mudar o conteudo da tupla
print('-'*50)

objetos[0] = "caneta" # Irá ocorrer um erro pois oa valores de uma tupla são imutáveis
print(objetos)