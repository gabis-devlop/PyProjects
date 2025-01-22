# Função: Venda de ingressos para um cinema
estoque_maximo = 6000
valor_ingresso = 20.00

while estoque_maximo > 0:
    try:
        idade = int(input('Digite sua idade (ou 0 para cancelar): '))
        if idade == 0:
            print("Cancelando a operação...")
            continue
    except ValueError:
        print('Idade inválida. Tente novamente.')
        continue

# condição para venda de ingressos com 3 opções de filmes
    if idade < 3:
        print('Ingresso gratuito')
        filmes = ['Moana']
    elif idade >= 3 and idade < 13:
        print('Ingresso com 50% de desconto')
        filmes = ['Meu Malvado Favorito', 'Zootopia']
    elif idade >= 13 and idade <= 17:
        print('Ingresso com 50% de desconto acompanhado de Carteirinha de Estudante')
        filmes = ['O Rei Leão - O filme', 'Toy Story 3']
    else:
        print('Ingresso inteiro')
        filmes = ['Coringa 2', 'Inception', 'Deadpool e Wolverine', 'Vingadores - O Ultimato', 'Aliens vs Predador']

    print('Filmes disponíveis:')
    for i, filme in enumerate(filmes, 1):
        print(f"{i} - {filme}")

    while True:
        try:
            escolha_filme = int(input("Escolha o número do filme (ou 0 para cancelar): "))
            if escolha_filme == 0:
                print("Cancelando a operação...")
                if quantidade_ingressos > 0:
                    break
            if escolha_filme < 1 or escolha_filme > len(filmes):
                print("Escolha inválida. Tente novamente.")
                continue
            filme_escolhido = filmes[escolha_filme - 1]
            break
        except ValueError:
            print("Escolha inválida. Tente novamente.")

    if escolha_filme == 0:
        continue

    while True:
        confirmacao = input(f"Você escolheu '{filme_escolhido}'. Confirmar? (s/n ou 0 para cancelar): ").lower()
        if confirmacao == '0':
            print("Cancelando a operação...")
            break
        if confirmacao == 's':
            break
        print("Escolha Inválida. Tente novamente.")

    if confirmacao == '0':
        continue

    while True:
        try:
            quantidade_ingressos = int(input("Digite a quantidade de ingressos (ou 0 para cancelar): "))
            if quantidade_ingressos == 0:
                print("Cancelando a operação...")
                break
            break
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número.")

    if quantidade_ingressos == 0:
        continue

# Verifica se a quantidade solicitada está dentro do limite do estoque
    if quantidade_ingressos > estoque_maximo:
        print(f"Desculpe, temos apenas {estoque_maximo} ingressos disponíveis.")
        quantidade_ingressos = estoque_maximo

# Calcula o valor total dos ingressos
    if idade < 3:
        valor_total = 0
    elif idade >= 3 and idade < 13:
        valor_total = quantidade_ingressos * (valor_ingresso / 2)
    elif idade >= 13 and idade <= 17:
        valor_total = quantidade_ingressos * (valor_ingresso / 2)
    else:
        valor_total = quantidade_ingressos * valor_ingresso

    print(f"Valor total: R${valor_total:.2f}")

    if idade >= 3:  # Apenas solicita forma de pagamento se a idade for maior ou igual a 3

        while True:
            print("Formas de pagamento disponíveis:\n1 - Crédito\n2 - Débito\n3 - Pix\n4 - Dinheiro")
            try:
                forma_pagamento = int(input("Escolha a forma de pagamento (1-4 ou 0 para cancelar): "))
                if forma_pagamento == 0:
                    print("Cancelando a operação...")
                    break
                if forma_pagamento in [1, 2, 3, 4]:
                    estoque_maximo -= quantidade_ingressos
                    print(f"Pagamento aprovado. Ingressos restantes: {estoque_maximo}")
                    break
                else:
                    print("Forma de pagamento inválida. Tente novamente.")
            except ValueError:
                print("Forma de pagamento inválida. Tente novamente.")

        if forma_pagamento == 0:
            continue
    else:
        print(f"Ingressos restantes: {estoque_maximo}")

    print("Tenha um bom filme!\n")

print("Estoque de ingressos esgotado.")

# Fim do programa