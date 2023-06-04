total = 0
compras = []

while True:
    item = input("Digite o nome do item: ")
    valor = float(input("Digite o valor do item: "))
    
    total += valor
    compras.append((item, valor))
    
    resposta = input("Deseja continuar comprando? (s/n): ")
    if resposta.lower() != "s":
        break

print("Suas compras:")
for item, valor in compras:
    print(f"{item}: R${valor:.2f}")

print(f"Total: R${total:.2f}")
