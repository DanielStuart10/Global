def menu_display():
    print("Digital Fair | Menu Principal: ")
    print("1 - Comprar")
    print("2 - Dados Cadastro")
    print("3 - Meu Cadastro")
    print("4 - Nova Assinatura")
    print("5 - Sair")
    

def fazer_compras():
    total = 0
    compras = []

    while True:
        item = input("Digite o nome do item: ")
        valor = float(input("Digite o valor do item: "))
        
        total += valor
        compras.append((item, valor))
        
        resposta = input("Deseja continuar comprando? (sim/não): ")
        if resposta.lower() != "sim":
            print("Voltando ao menu")
            break

    print("Obrigado por comprar conosco! \nSuas compras:")
    for item, valor in compras:
        print(f"{item}: R${valor:.2f}")

    print(f"Total: R${total:.2f}")

def cadastrar(lista_cadastros):
    print("Preencha as informações:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o e-mail: ")

    cadastro = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    lista_cadastros.append(cadastro)
    print("Cadastro realizado com sucesso!")


def meu_cadastro(lista_cadastros):
    if lista_cadastros:
        print("Informações do cadastro")
        for cadastro in lista_cadastros:
            print("Nome:", cadastro["nome"])
            print("Idade:", cadastro["idade"])
            print("E-mail:", cadastro["email"])
            print("---------------------------")
    else:
        print("Nenhum cadastro encontrado.")

def assinatura():
    while True:
        resposta = input("Deseja criar uma nova assinatura? (sim/não): ")
        
        if resposta.lower() == "não":
            return
        
        if resposta.lower() == "sim":
            produtos = []
            quantidade = int(input("Quantos produtos você deseja adicionar? "))
            
            for i in range(quantidade):
                produto = input(f"Digite o nome do produto {i+1}: ")
                produtos.append(produto)
            
            frequencia = input("Escolha a frequência (1 - Mensal, 2 - Bimestral, 3 - Trimestral): ")
            
            if frequencia == "1":
                frequencia_texto = "mensal"
            elif frequencia == "2":
                frequencia_texto = "bimestral"
            elif frequencia == "3":
                frequencia_texto = "trimestral"
            else:
                print("Frequência inválida. A assinatura não foi concluída.")
                continue
            
            print("Assinatura concluída com sucesso!")
            
            resposta = input("Deseja criar outra assinatura? (sim/não): ")
            
            if resposta.lower() == "não":
                return


def main():
    lista_cadastros = []
    assinaturas = []

    while True:
        menu_display()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            fazer_compras()
        elif escolha == "2":
            cadastrar(lista_cadastros)
        elif escolha == "3":
            meu_cadastro(lista_cadastros)
        elif escolha == "4":
            assinatura()
        elif escolha == "5":
            print("Obrigado por escolher Digital Fair")
            break
        else:
            print("Escolha inválida, tente novamente")

main()



