print("Cadastro do Primeiro usuário")
while True:
    loginU1 = input("login: ")
    senhaU1 = input("senha: ")
    if loginU1!= senhaU1:
        break
    print("O login e a senha não podem ser os mesmos. Tente novamente.")
print("Cadastro do Segundo usuario")
while True:
    loginU2 = input("login: ")
    senhaU2 = input("senha: ")
    if loginU2!= senhaU2 and loginU2 != loginU1:
        break
    if loginU2 == senhaU2:
        print("O login e a senha não podem ser os mesmos. Tente novamente.")
    else:
        print("Os logins dos usuários não podem ser iguais. ente novamente.")
print("Cadastros bem sucedidos!")