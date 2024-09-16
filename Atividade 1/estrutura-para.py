

'''
estrutura de repetição e mias comum em qualuqer outra linguagem de programação 

for (contador =1; contador <=5; contador++){
}
'''
#1 exemplo
for contador in range (1,6):
    print(contador)

print("-"*30)
#2 exemplo
for contador in range (1,11,2): # o 3 parametro irá aumentar o incremento dos valores que estao sendo exibidors
    print(contador)
print("-"*30)

#3 exemplo
for contador in rage (10,0,-1):
    print(contador,end="") #o comando end, informa