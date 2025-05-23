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

#Função para escolher o cenário
def escolher_cenario():
    print("🌍 Escolha o cenário da batalha:")
    for i, nome in enumerate(CENARIOS, 1):
        print(f"{i}. {nome.title()}")
    while True:
        try:
            opcao = int(input("Digite o número do cenário: "))
            if 1 <= opcao <= len(CENARIOS):
                return list(CENARIOS.keys())[opcao - 1]
            else:
                print("⚠️ Escolha inválida.")
        except ValueError:
            print("⚠️ Digite um número válido.")