# Função: Venda de ingressos para um cinema
estoque_maximo = 6000
valor_ingresso = 20.00

while estoque_maximo > 0:
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Idade inválida. Tente novamente.')
        continue

# condição para venda de ingressos com 3 opções de filmes
    if idade < 3:
        print('Ingresso gratuito')
        print('Filmes disponíveis: \n1 - Moana')
    elif idade >= 3 and idade < 13:
        print('Ingresso com 50% de desconto')
        print('Filmes disponíveis: \n1 - Meu malvado Favorito \n2 - Zootopia')
    elif idade >= 13 and idade <= 17:
        print('Ingresso com 50% de desconto acompanhado de Carteirinha de Estudante')
        print('Filmes disponíveis: \n1 - O Rei Leão - O filme  \n2 - Toy Story 3')
    else:
        print('Ingresso inteiro')
        print('Filmes disponíveis: \n1 - Coringa 2 \n2 - Inception \n3 - Deadpool e Wolverine \n4 - Vingadores - O Ultimato \n5 - Aliens vs Predador')

    try:
        quantidade_ingressos = int(input("Digite a quantidade de ingressos: "))
    except ValueError:
        print("Quantidade inválida. Por favor, insira um número.")
        continue

# Verifica se a quantidade solicitada está dentro do limite do estoque
    if quantidade_ingressos > estoque_maximo:
        print(f"Desculpe, temos apenas {estoque_maximo} ingressos disponíveis.")
        quantidade_ingressos = estoque_maximo

# Calcula o valor total dos ingressos
    valor_total = quantidade_ingressos * valor_ingresso
    print(f"Valor total: R${valor_total:.2f}")

# Simula forma de pagamento
    forma_pagamento = input("Digite 'c' para crédito, 'd' para débito ou 'p' para Pix: ").lower()

    if forma_pagamento in ['c', 'd', 'p']:
        estoque_maximo -= quantidade_ingressos
        print(f"Pagamento aprovado. Ingressos restantes: {estoque_maximo}")
    else:
        print("Forma de pagamento inválida. Tente novamente.")

    print("Tenha um bom filme!\n")

print("Estoque de ingressos esgotado.")

# Fim do programa