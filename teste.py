def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o e-mail: ")

    # Criar um dicionário com os dados do cadastro
    cadastro = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    # Armazenar o cadastro em uma lista
    lista_cadastros.append(cadastro)
    print("Cadastro realizado com sucesso!")


# Lista para armazenar os cadastros
lista_cadastros = []

# Exemplo de uso da função
cadastrar()
