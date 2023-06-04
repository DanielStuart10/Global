def assinatura(lista_cadastros):
    resposta = input("Deseja criar uma nova assinatura? (sim/não): ")
    
    if resposta.lower() == "não":
        return None
    elif resposta.lower() != "sim":
        print("Resposta inválida. A assinatura não será criada.")
        return None
    
    produtos = []
    while True:
        produto = input("Digite o nome do produto (ou deixe em branco para encerrar): ")
        if produto == "":
            break
        produtos.append(produto)
    
    frequencia = input("Digite a frequência desejada (1 - mensal, 2 - bimestral, 3 - trimestral): ")
    while frequencia not in ["1", "2", "3"]:
        print("Opção inválida. Tente novamente.")
        frequencia = input("Digite a frequência desejada (1 - mensal, 2 - bimestral, 3 - trimestral): ")
    
    assinatura = {
        "produtos": produtos,
        "frequencia": int(frequencia)
    }
    
    print("Assinatura concluída com sucesso!")
    return assinatura
