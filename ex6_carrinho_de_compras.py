# Define a constante para a taxa de juros do cartão de crédito
TAXA_JUROS_CREDITO = 0.03

def exibir_carrinho(itens_comprados, total, compra_confirmada=False):
    # Função para exibir os itens no carrinho ou os itens comprados.
    if compra_confirmada:
        print("\nItens comprados:")  # Exibe esta mensagem se a compra foi confirmada.
        print(f"Total final: R$ {total:.2f}")
    else:
        print("\nItens no carrinho:")  # Exibe esta mensagem se a compra não foi confirmada.
    
    # Itera sobre cada item na lista de itens comprados.
    for item, preco in itens_comprados:
        print(f"{item}: R$ {preco:.2f}")  # Exibe o nome do item e seu preço formatado.
    
    # Exibe o total acumulado dos itens.
    print(f"Total: R$ {total:.2f}")

def realizar_compra():
    continua = "s"  # Variável de controle para continuar a compra.
    total = 0  # Inicializa o total da compra.
    itens_comprados = []  # Inicializa a lista de itens comprados.

    # Loop para continuar a compra até o usuário decidir parar.
    while continua.lower() == "s":
        try:
            # Solicita ao usuário que escolha uma ação.
            acao = int(input("\nEscolha uma ação: [1] Adicionar item, [2] Remover último item, [3] Exibir carrinho: "))
        except ValueError:
            print("Ação inválida. Por favor, escolha uma opção válida.")
            continue

        # Verifica qual ação o usuário escolheu e chama a função correspondente.
        if acao == 1:
            itens_comprados, total = adicionar_item(itens_comprados, total)
        elif acao == 2:
            itens_comprados, total = remover_item(itens_comprados, total)
        elif acao == 3:
            exibir_carrinho(itens_comprados, total)
        else:
            print("Ação inválida. Por favor, escolha uma opção válida.")

        # Pergunta ao usuário se deseja continuar realizando ações.
        continua = input("\nDeseja realizar outra ação? (s/n) ")

    # Exibe o carrinho final após o usuário decidir parar de adicionar ou remover itens.
    exibir_carrinho(itens_comprados, total)
    
    # Solicita ao usuário que escolha a forma de pagamento.
    forma_pagamento = escolher_forma_pagamento()

    # Processa o pagamento de acordo com a forma escolhida.
    if forma_pagamento == 1:
        total = processar_pagamento_dinheiro(itens_comprados, total)
    elif forma_pagamento == 2:
        total = processar_pagamento_credito(itens_comprados, total)

    # Confirma a compra após o processamento do pagamento.
    confirmar_compra(itens_comprados, total, forma_pagamento)

def adicionar_item(itens_comprados, total):
    item = input("Informe o nome do item: ")  # Solicita o nome do item ao usuário.
    
    # Loop para validar a entrada do preço do item.
    while True:
        try:
            preco = float(input("Informe o preço do item: "))  # Solicita o preço do item ao usuário.
            if preco <= 0:
                print("Preço inválido. O preço deve ser um valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, informe um valor numérico.")

    # Adiciona o item e seu preço à lista de itens comprados.
    itens_comprados.append((item, preco))
    total += preco  # Atualiza o total da compra.
    return itens_comprados, total

def remover_item(itens_comprados, total):
    # Verifica se há itens na lista de itens comprados para remover.
    if itens_comprados:
        item, preco = itens_comprados.pop()  # Remove o último item adicionado.
        total -= preco  # Atualiza o total da compra.
        print(f"Item {item} removido.")  # Informa qual item foi removido.
    else:
        print("Nenhum item para remover.")  # Informa que não há itens para remover.
    return itens_comprados, total

def escolher_forma_pagamento():
    """
    Solicita ao usuário que escolha a forma de pagamento e valida a entrada.
    
    Retorna:
        int: O número correspondente à forma de pagamento escolhida.
    """
    print("\nEscolha a forma de pagamento:")
    print("[1] Dinheiro")
    print("[2] Cartão de crédito")
    print("[3] Cartão de débito")
    print("[4] Pix")
    
    # Loop para validar a entrada da forma de pagamento.
    while True:
        try:
            forma_pagamento = int(input("Informe a forma de pagamento: "))
            if forma_pagamento in [1, 2, 3, 4]:
                break
            else:
                print("Forma de pagamento inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, informe um valor numérico.")
    return forma_pagamento

def processar_pagamento_dinheiro(itens_comprados, total):
    """
    Processa o pagamento em dinheiro, calcula o troco e confirma a compra.

    Args:
        itens_comprados (list): Lista de itens comprados.
        total (float): Total da compra.

    Returns:
        float: O total da compra após o processamento do pagamento.
    """
    while True:
        try:
            valor_pago = float(input("Informe o valor pago: "))  # Solicita o valor pago ao usuário.
            if valor_pago < total:
                print("Valor pago insuficiente. Por favor, pague o valor total ou mais.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, informe um valor numérico.")

    troco = valor_pago - total  # Calcula o troco.
    print(f"Troco: R$ {troco:.2f}")
    confirmar_compra(itens_comprados, total, 1, troco)
    return total

def processar_pagamento_credito(itens_comprados, total):
    """
    Processa o pagamento com cartão de crédito, calcula os juros e confirma a compra.

    Args:
        itens_comprados (list): Lista de itens comprados.
        total (float): Total da compra.

    Returns:
        float: O total da compra após a inclusão dos juros do cartão de crédito.
    """
    while True:
        try:
            parcelas = int(input("Deseja dividir em quantas vezes? (1-3): "))  # Solicita o número de parcelas ao usuário.
            if parcelas in [1, 2, 3]:
                break
            else:
                print("Número de parcelas inválido. Escolha entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, informe um valor numérico.")
    
    total_com_juros = total * (1 + TAXA_JUROS_CREDITO)  # Calcula o total com juros.
    valor_parcela = total_com_juros / parcelas  # Calcula o valor de cada parcela.
    print(f"Compra dividida em {parcelas}x de R$ {valor_parcela:.2f} (Total com juros: R$ {total_com_juros:.2f})")
    return total_com_juros

def confirmar_compra(itens_comprados, total, forma_pagamento, troco=0):
    """
    Confirma a compra, exibe os detalhes e agradece ao cliente.

    Args:
        itens_comprados (list): Lista de itens comprados.
        total (float): Total da compra.
        forma_pagamento (int): Forma de pagamento escolhida.
        troco (float, optional): Troco a ser devolvido, se houver. Default é 0.
    """
    confirmacao = input("Deseja confirmar a compra? (s/n) ")  # Solicita confirmação da compra ao usuário.
    if confirmacao.lower() == 's':
        print("\nCompra confirmada!")
        exibir_carrinho(itens_comprados, total, compra_confirmada=True)
        if forma_pagamento == 1:
            print(f"Troco: R$ {troco:.2f}")
        print("Pagamento realizado com sucesso.")
        print("Obrigado pela sua compra!")
    else:
        print("Compra cancelada.")

# Loop principal para iniciar o processo de compra.
while True:
    realizar_compra()
    repetir = input("Deseja realizar outra compra? (s/n) ")
    if repetir.lower() != 's':
        break
