print("Cadastro do Primeiro usuário")

while True:
    loginUser_1 = input("login: ")
    senhaUser_1 = input("senha: ")
    if loginUser_1!= senhaUser_1:
        break
    print("O login e a senha não podem ser os mesmos. Tente novamente.")

print("Cadastro do Segundo usuario")


while True:
    loginUser_2 = input("login: ")
    senhaUser_2 = input("senha: ")
    if loginUser_2!= senhaUser_2 and loginUser_2 != loginUser_1:
        break
    if loginUser_2 == senhaUser_2:
        print("O login e a senha não podem ser os mesmos. Tente novamente.")
    else:
        print("Os logins dos usuários não podem ser iguais. ente novamente.")

print("Cadastros bem sucedidos!")
    
