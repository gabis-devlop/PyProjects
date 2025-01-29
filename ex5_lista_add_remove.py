# Função para exibir a lista de tarefas atualizada
def exibir_lista(lista):
    print("\nLista de tarefas atualizada:")

# Enumerar as tarefas na lista para facilitar a remoção pelo índice
    for indice, tarefa in enumerate(lista, 1):
        print(f"{indice}. {tarefa}")
    print()
    
# Função principal do programa
def main():
    lista_de_tarefas = []  # Inicializa uma lista vazia
    
    while True:  # Loop infinito para continuar solicitando ações do usuário
        exibir_lista(lista_de_tarefas)  # Exibir a lista de tarefas antes de cada ação
        # Opções de ação para o usuário
        print("Escolha uma ação:")
        print("1. Adicionar uma tarefa")
        print("2. Remover uma tarefa")
        print("3. Sair")
        
    # Solicita a escolha do usuário
        escolha = input("Digite o número da ação desejada: ")
        
        if escolha == '1':  # Adicionar uma tarefa à lista
            tarefa = input("Digite a tarefa a ser adicionada: ")
            lista_de_tarefas.append(tarefa)  # Adiciona a tarefa à lista
        elif escolha == '2':  # Remover uma tarefa da lista
            try:  # Utiliza try-except para lidar com possíveis erros de entrada
                exibir_lista(lista_de_tarefas)  # Exibe a lista de tarefas para o usuário
                indice_para_remover = int(input("Digite o número da tarefa a ser removida: ")) - 1
                # Remove a tarefa pelo índice fornecido pelo usuário
                lista_de_tarefas.pop(indice_para_remover)
            except (ValueError, IndexError):  # Captura erros de número inválido
                print("Número inválido. Tente novamente.")
        elif escolha == '3':  # Sair do programa
            print("Saindo do programa...")
            break  # Interrompe o loop para terminar o programa
        else:
            print("Escolha inválida. Tente novamente.")  # Mensagem para entrada inválida
            
if __name__ == "__main__":
    main()  # Chamando a função principal
