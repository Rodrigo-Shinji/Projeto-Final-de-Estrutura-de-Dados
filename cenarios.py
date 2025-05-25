# Dicionário CENARIOS: Armazena a configuração de diferentes cenários de batalha.
# Cada cenário é uma chave (nome do cenário) e seu valor é um dicionário contendo:
# - "bonus": Uma lista de elementos que recebem bônus de força neste cenário.
# - "penalidade": Uma lista de elementos que sofrem penalidade de força neste cenário.
# - "bonus_valor": O valor de força a ser adicionado para elementos com bônus.
# - "penalidade_valor": O valor de força a ser subtraído para elementos com penalidade.
CENARIOS = {
    "vulcao": {"bonus": ["fogo", "terra"], "penalidade": ["agua", "vento"], "bonus_valor": 2000, "penalidade_valor": 500},
    "inferno": {"bonus": ["fogo", "trevas"], "penalidade": ["agua", "luz"], "bonus_valor": 2400, "penalidade_valor": 700},
    "caverna": {"bonus": ["trevas", "terra"], "penalidade": ["luz", "vento"], "bonus_valor": 3200, "penalidade_valor": 400},
    "mar": {"bonus": ["agua", "vento"], "penalidade": ["fogo", "trevas"], "bonus_valor": 3000, "penalidade_valor": 320},
    "montanha": {"bonus": ["vento", "luz"], "penalidade": ["agua", "luz"], "bonus_valor": 1300, "penalidade_valor": 500},
    "ceus": {"bonus": ["luz", "vento"], "penalidade": ["trevas", "terra"], "bonus_valor": 2800, "penalidade_valor": 1000},
    "iceberg": {"bonus": ["agua", "luz"], "penalidade": ["fogo", "luz"], "bonus_valor": 1600, "penalidade_valor": 700},
    "deserto": {"bonus": ["luz", "terra"], "penalidade": ["agua", "trevas"], "bonus_valor": 2400, "penalidade_valor": 650},
    "riacho": {"bonus": ["agua", "vento"], "penalidade": ["luz", "fogo"], "bonus_valor": 850, "penalidade_valor": 400},
    "tempestade": {"bonus": ["trevas", "vento"], "penalidade": ["luz", "terra"], "bonus_valor": 3500, "penalidade_valor": 700},
    "espaco": {"bonus": ["luz", "trevas"], "penalidade": ["terra", "agua"], "bonus_valor": 4050, "penalidade_valor": 350},
    "floresta em chamas": {"bonus": ["fogo", "vento"], "penalidade": ["agua", "terra"], "bonus_valor": 2100, "penalidade_valor": 490},
}

def escolher_cenario():
    """
    Apresenta uma lista de cenários disponíveis e permite que o usuário escolha um.
    Retorna o nome do cenário escolhido.
    """
    print("Escolha o cenário da batalha:")
    # Itera sobre os cenários e exibe cada um com um número correspondente.
    for i, nome in enumerate(CENARIOS, 1):
        print(f"{i}. {nome.title()}") # .title() capitaliza a primeira letra de cada palavra

    while True: # Loop contínuo até que uma opção válida seja escolhida.
        try:
            # Solicita ao usuário que digite o número do cenário.
            opcao = int(input("Digite o número do cenário: "))
            # Verifica se a opção está dentro do intervalo válido de cenários.
            if 1 <= opcao <= len(CENARIOS):
                # Retorna o nome do cenário correspondente à opção escolhida.
                # list(CENARIOS.keys())[opcao - 1] converte as chaves do dicionário em uma lista e acessa pelo índice.
                return list(CENARIOS.keys())[opcao - 1]
            else:
                print("Escolha inválida.") # Mensagem de erro para opção fora do intervalo.
        except ValueError:
            print("Digite um número válido.") # Mensagem de erro para entrada não numérica.