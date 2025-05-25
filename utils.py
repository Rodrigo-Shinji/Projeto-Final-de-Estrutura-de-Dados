def menu_principal():
    """
    Exibe o menu principal da aplicação e solicita a escolha do usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\n=== MENU PRINCIPAL ===") # Título do menu.
    print("1. Gerenciar Personagens") # Opção para acessar o menu de personagens.
    print("2. Gerenciar Times")       # Opção para acessar o menu de times.
    print("3. Iniciar Batalha (PvP)") # Opção para iniciar uma batalha entre times.
    print("4. Ver Histórico de Batalhas") # Opção para visualizar o histórico de batalhas.
    print("0. Sair")                  # Opção para encerrar a aplicação.
    return input("Escolha uma opção: ") # Solicita e retorna a entrada do usuário.

def menu_personagens():
    """
    Exibe o menu de gerenciamento de personagens e solicita a escolha do usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\n=== MENU DE PERSONAGENS ===") # Título do menu de personagens.
    print("1. Cadastrar Personagem")  # Opção para adicionar um novo personagem.
    print("2. Excluir Personagem")    # Opção para remover um personagem existente.
    print("3. Listar Personagens")    # Opção para ver todos os personagens cadastrados.
    print("4. Editar Personagem")     # Opção para modificar os dados de um personagem.
    print("0. Voltar")                # Opção para retornar ao menu principal.
    return input("Escolha uma opção: ") # Solicita e retorna a entrada do usuário.

def menu_times():
    """
    Exibe o menu de gerenciamento de times e solicita a escolha do usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\n=== MENU DE TIMES ===") # Título do menu de times.
    print("1. Criar Time")            # Opção para criar um novo time.
    print("2. Excluir Time")          # Opção para remover um time existente.
    print("3. Listar Times")          # Opção para ver todos os times cadastrados.
    print("4. Inserir Personagem no Time") # Opção para adicionar um personagem a um time.
    print("5. Remover Personagem do Time") # Opção para remover um personagem de um time.
    print("6. Listar Personagens de um Time") # Opção para ver os personagens de um time específico.
    print("0. Voltar")                # Opção para retornar ao menu principal.
    return input("Escolha uma opção: ") # Solicita e retorna a entrada do usuário.

def entrada_inteiro(msg):
    """
    Solicita uma entrada do usuário e garante que seja um número inteiro.
    Continua solicitando até que uma entrada válida seja fornecida.

    Args:
        msg (str): A mensagem a ser exibida ao usuário antes da entrada.

    Returns:
        int: O valor inteiro digitado pelo usuário.
    """
    while True: # Loop infinito que só é interrompido quando uma entrada válida é fornecida.
        try:
            valor = int(input(msg)) # Tenta converter a entrada do usuário para um inteiro.
            return valor           # Se a conversão for bem-sucedida, retorna o valor.
        except ValueError: # Captura o erro se a entrada não puder ser convertida para inteiro.
            print("Valor inválido. Digite um número inteiro.") # Mensagem de erro.

def entrada_nome(msg):
    """
    Solicita uma entrada de nome do usuário e garante que não seja vazia.
    Remove espaços em branco no início e fim da string.

    Args:
        msg (str): A mensagem a ser exibida ao usuário antes da entrada.

    Returns:
        str: O nome digitado pelo usuário (sem espaços extras e não vazio).
    """
    nome = input(msg).strip() # Solicita a entrada e remove espaços em branco (início/fim) com .strip().
    while not nome: # Loop que continua enquanto o nome estiver vazio (após o .strip()).
        print("Nome não pode ser vazio.") # Mensagem de erro.
        nome = input(msg).strip() # Solicita a entrada novamente.
    return nome # Retorna o nome validado.