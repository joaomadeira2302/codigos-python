# Função para cadastrar um usuário com validação de login e senha
def cadastrar_usuario(usuarios_cadastrados):
    while True:
        login = input("Digite o login desejado: ")
        
        # Verifica se o login já foi usado por outro usuário
        if login in usuarios_cadastrados:
            print("Esse login já está sendo usado. Escolha outro.")
            continue
        
        while True:
            senha = input("Digite a senha desejada: ")
            
            # Verifica se o login e a senha são iguais
            if login == senha:
                print("Login e senha não podem ser iguais. Tente novamente.")
            else:
                break  # Senha válida, sair do loop de senha
        
        # Adiciona o login e senha válidos ao dicionário de usuários cadastrados
        usuarios_cadastrados[login] = senha
        print("Usuário cadastrado com sucesso!\n")
        break  # Login e senha válidos, sair do loop de login

# Dicionário para armazenar os usuários cadastrados
usuarios_cadastrados = {}

# Cadastro do primeiro usuário
print("Cadastro do primeiro usuário:")
cadastrar_usuario(usuarios_cadastrados)

# Cadastro do segundo usuário
print("Cadastro do segundo usuário:")
cadastrar_usuario(usuarios_cadastrados)

# Exibindo os usuários cadastrados (opcional)
print("Usuários cadastrados:", usuarios_cadastrados)
