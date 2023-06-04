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
            frequencia_texto = "Mensal"
        elif frequencia == 2:
            frequencia_texto = "Bimestral"
        elif frequencia == 3:
            frequencia_texto = "Trimestral"
        else:
            print("Opção inválida. Assinatura não criada.")
            return
        
        nova_assinatura = {"produtos": produtos, "frequencia": frequencia_texto}
        
        return nova_assinatura
    else:
        print("Nenhuma assinatura será criada.")
        return None

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

# Lista para armazenar as assinaturas
assinaturas = []

# Laço principal para interação com o usuário
while True:
    nova_assinatura = assinatura()
    
    if nova_assinatura is not None:
        assinaturas.append(nova_assinatura)
    
    listar_assinaturas(assinaturas)
    
    continuar = input("Deseja continuar? (sim/não): ")
    
    if continuar.lower() != "sim":
        break
