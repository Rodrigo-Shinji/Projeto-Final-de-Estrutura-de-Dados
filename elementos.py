VANTAGENS = {
    "fogo": ["terra"],
    "agua": ["fogo"],
    "luz": ["fogo"],
    "vento": ["luz"],
    "terra": ["vento"],
    "trevas": ["luz"]
}

DESVANTAGENS = {
    "fogo": ["agua"],
    "agua": ["luz"],
    "luz": ["trevas"],
    "vento": ["terra"],
    "terra": ["fogo"],
    "trevas": ["terra"]
}

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

def ajustar_forca_com_elementos(personagem, oponentes):
    """Ajusta a força do personagem com base em vantagem ou desvantagem contra oponentes."""
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    vantagem = sum(1 for o in oponentes if o["elemento"] in VANTAGENS.get(elemento, []))
    desvantagem = sum(1 for o in oponentes if o["elemento"] in DESVANTAGENS.get(elemento, []))

    # Define os bônus e penalidades
    bonus = 1000 * vantagem
    penalidade = 500 * desvantagem

    return forca + bonus - penalidade


def aplicar_cenario(personagem, cenario_nome):
    cenario = CENARIOS.get(cenario_nome.lower())
    if not cenario:
        return personagem["forca"]
    
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    if elemento in cenario["bonus"]:
        forca += cenario["bonus_valor"]
    if elemento in cenario["penalidade"]:
        forca -= cenario["penalidade_valor"]

    return forca