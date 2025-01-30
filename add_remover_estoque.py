carros = []

def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar carro")
    print("2. Remover carro")
    print("3. Listar carros")
    print("4. Sair")

def adicionar_carro():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    carros.append({"marca": marca, "modelo": modelo, "ano": ano})
    print(f"Carro {modelo} adicionado com sucesso!")

def remover_carro():
    if not carros:
        print("Nenhum carro para remover.")
        return
    listar_carros()
    indice = int(input("Digite o número do carro que deseja remover: ")) - 1
    if 0 <= indice < len(carros):
        carro_removido = carros.pop(indice)
        print(f"Carro {carro_removido['modelo']} removido com sucesso!")
    else:
        print("Número inválido!")

def listar_carros():
    if not carros:
        print("Nenhum carro no estoque.")
    else:
        print("\nCarros no estoque:")
        for i, carro in enumerate(carros, 1):
            print(f"{i}. Marca: {carro['marca']}, Modelo: {carro['modelo']}, Ano: {carro['ano']}")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_carro()
    elif opcao == "2":
        remover_carro()
    elif opcao == "3":
        listar_carros()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")