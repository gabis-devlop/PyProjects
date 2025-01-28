def exibir_carrinho(itens_comprados, total, compra_confirmada=False):
    if compra_confirmada:
        print("\nItens comprados:")
    else:
        print("\nItens no carrinho:")
    for item, preco in itens_comprados:
        print(f"{item}: R$ {preco:.2f}")
    print(f"Total: R$ {total:.2f}")

def realizar_compra():
    continua = "s"
    total = 0
    itens_comprados = []

    while continua.lower() == "s":
        acao = input("\nEscolha uma ação: [1] Adicionar item, [2] Remover último item, [3] Exibir carrinho: ")
        if acao == "1":
            itens_comprados, total = adicionar_item(itens_comprados, total)
        elif acao == "2":
            itens_comprados, total = remover_item(itens_comprados, total)
        elif acao == "3":
            exibir_carrinho(itens_comprados, total)
        else:
            print("Ação inválida. Por favor, escolha uma opção válida.")

        continua = input("\nDeseja realizar outra ação? (s/n) ")

    exibir_carrinho(itens_comprados, total)

    forma_pagamento = escolher_forma_pagamento()

    if forma_pagamento == 1:
        processar_pagamento_dinheiro(itens_comprados, total)
    elif forma_pagamento == 2:
        total = processar_pagamento_credito(itens_comprados, total)
        confirmar_compra(itens_comprados, total, forma_pagamento)
    else:
        confirmar_compra(itens_comprados, total, forma_pagamento)

def adicionar_item(itens_comprados, total):
    item = input("Informe o nome do item: ")
    preco = float(input("Informe o preço do item: "))
    while preco <= 0:
        print("Preço inválido. O preço deve ser um valor positivo.")
        preco = float(input("Informe o preço do item: "))
    itens_comprados.append((item, preco))
    total += preco
    return itens_comprados, total

def remover_item(itens_comprados, total):
    if itens_comprados:
        item, preco = itens_comprados.pop()
        total -= preco
        print(f"Item {item} removido.")
    else:
        print("Nenhum item para remover.")
    return itens_comprados, total

def escolher_forma_pagamento():
    print("\nEscolha a forma de pagamento:")
    print("[1] Dinheiro")
    print("[2] Cartão de crédito")
    print("[3] Cartão de débito")
    print("[4] Pix")
    forma_pagamento = int(input("Informe a forma de pagamento: "))
    while forma_pagamento not in [1, 2, 3, 4]:
        print("Forma de pagamento inválida.")
        forma_pagamento = int(input("Informe a forma de pagamento (1-4): "))
    return forma_pagamento

def processar_pagamento_dinheiro(itens_comprados, total):
    valor_pago = float(input("Informe o valor pago: "))
    while valor_pago < total:
        print("Valor pago insuficiente.")
        valor_pago = float(input("Informe o valor pago: "))
    troco = valor_pago - total
    print(f"Troco: R$ {troco:.2f}")
    confirmar_compra(itens_comprados, total, 1, troco)

def processar_pagamento_credito(itens_comprados, total):
    parcelas = int(input("Deseja dividir em quantas vezes? (1-3): "))
    while parcelas not in [1, 2, 3]:
        print("Número de parcelas inválido. Escolha entre 1 e 3.")
        parcelas = int(input("Deseja dividir em quantas vezes? (1-3): "))
    total_com_juros = total * 1.03
    valor_parcela = total_com_juros / parcelas
    print(f"Compra dividida em {parcelas}x de R$ {valor_parcela:.2f} (Total com juros: R$ {total_com_juros:.2f})")
    return total_com_juros

def confirmar_compra(itens_comprados, total, forma_pagamento, troco=0):
    confirmacao = input("Deseja confirmar a compra? (s/n) ")
    if confirmacao.lower() == 's':
        print("\nCompra confirmada!")
        exibir_carrinho(itens_comprados, total, compra_confirmada=True)
        if forma_pagamento == 1:
            print(f"Troco: R$ {troco:.2f}")
        print("Pagamento realizado com sucesso.")
        print("Obrigado pela sua compra!")
    else:
        print("Compra cancelada.")

while True:
    realizar_compra()
    repetir = input("Deseja realizar outra compra? (s/n) ")
    if repetir.lower() != 's':
        break
