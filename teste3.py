def assinatura():
    criar_assinatura = input("Deseja criar uma nova assinatura? (sim/não): ")
    
    if criar_assinatura.lower() == "sim":
        produtos = []
        quantidade = int(input("Quantos produtos você deseja? "))
        
        for i in range(quantidade):
            produto = input("Digite o nome do produto: ")
            produtos.append(produto)
        
        frequencia = int(input("Escolha a frequência desejada:\n1 - Mensal\n2 - Bimestral\n3 - Trimestral\n"))
        
        if frequencia == 1:
            print("Assinatura criada com sucesso! Frequência: Mensal")
        elif frequencia == 2:
            print("Assinatura criada com sucesso! Frequência: Bimestral")
        elif frequencia == 3:
            print("Assinatura criada com sucesso! Frequência: Trimestral")
        else:
            print("Opção inválida. Assinatura não criada.")
    else:
        print("Nenhuma assinatura será criada.")

# Chamada da função assinatura
assinatura()


def listar_assinaturas(assinaturas):
    if len(assinaturas) == 0:
        print("Você ainda não possui assinaturas criadas.")
    else:
        print("Suas assinaturas:")
        for i, assinatura in enumerate(assinaturas, start=1):
            print(f"Assinatura {i}:")
            print("Produtos:", ", ".join(assinatura["produtos"]))
            print("Frequência:", assinatura["frequencia"])
            print()

# Exemplo de uso da função listar_assinaturas
ass1 = {"produtos": ["Produto A", "Produto B"], "frequencia": "Mensal"}
ass2 = {"produtos": ["Produto C"], "frequencia": "Bimestral"}
ass3 = {"produtos": ["Produto D", "Produto E", "Produto F"], "frequencia": "Trimestral"}

assinaturas = [ass1, ass2, ass3]

listar_assinaturas(assinaturas)
