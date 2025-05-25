# Dicionário VANTAGENS: Define as relações de vantagem elementais.
# Cada chave é um elemento e seu valor é uma tupla (para imutabilidade)
# de elementos contra os quais ele tem vantagem.
VANTAGENS = {
    "fogo": ("terra",),
    "agua": ("fogo",),
    "luz": ("fogo",),
    "vento": ("luz",),
    "terra": ("vento",),
    "trevas": ("luz",)
}

# Dicionário DESVANTAGENS: Define as relações de desvantagem elementais.
# Cada chave é um elemento e seu valor é uma tupla (para imutabilidade)
# de elementos contra os quais ele tem desvantagem.
DESVANTAGENS = {
    "fogo": ("agua",),
    "agua": ("luz",),
    "luz": ("trevas",),
    "vento": ("terra",),
    "terra": ("fogo",),
    "trevas": ("terra",)
}

# Dicionário CENARIOS: Define os modificadores de força com base no cenário da batalha.
# Cada chave é o nome do cenário e seu valor é um dicionário contendo:
# - "bonus": Um conjunto (set) de elementos que recebem bônus de força. Sets são eficientes para verificar pertinência.
# - "penalidade": Um conjunto (set) de elementos que sofrem penalidade de força.
# - "bonus_valor": O valor numérico do bônus.
# - "penalidade_valor": O valor numérico da penalidade.
CENARIOS = {
    "vulcao": {"bonus": {"fogo", "terra"}, "penalidade": {"agua", "vento"}, "bonus_valor": 2000, "penalidade_valor": 500},
    "inferno": {"bonus": {"fogo", "trevas"}, "penalidade": {"agua", "luz"}, "bonus_valor": 2400, "penalidade_valor": 700},
    "caverna": {"bonus": {"trevas", "terra"}, "penalidade": {"luz", "vento"}, "bonus_valor": 3200, "penalidade_valor": 400},
    "mar": {"bonus": {"agua", "vento"}, "penalidade": {"fogo", "trevas"}, "bonus_valor": 3000, "penalidade_valor": 320},
    "montanha": {"bonus": {"vento", "luz"}, "penalidade": {"agua", "luz"}, "bonus_valor": 1300, "penalidade_valor": 500},
    "ceus": {"bonus": {"luz", "vento"}, "penalidade": {"trevas", "terra"}, "bonus_valor": 2800, "penalidade_valor": 1000},
    "iceberg": {"bonus": {"agua", "luz"}, "penalidade": {"fogo", "luz"}, "bonus_valor": 1600, "penalidade_valor": 700},
    "deserto": {"bonus": {"luz", "terra"}, "penalidade": {"agua", "trevas"}, "bonus_valor": 2400, "penalidade_valor": 650},
    "riacho": {"bonus": {"agua", "vento"}, "penalidade": ["luz", "fogo"], "bonus_valor": 850, "penalidade_valor": 400},
    "tempestade": {"bonus": {"trevas", "vento"}, "penalidade": {"luz", "terra"}, "bonus_valor": 3500, "penalidade_valor": 700},
    "espaco": {"bonus": {"luz", "trevas"}, "penalidade": {"terra", "agua"}, "bonus_valor": 4050, "penalidade_valor": 350},
    "floresta em chamas": {"bonus": {"fogo", "vento"}, "penalidade": ["agua", "terra"], "bonus_valor": 2100, "penalidade_valor": 490},
}

def ajustar_forca_com_elementos(personagem, oponentes):
    """
    Ajusta a força do personagem com base em vantagem ou desvantagem contra oponentes.
    Calcula bônus se o elemento do personagem tiver vantagem contra o elemento de um oponente,
    e penalidades se tiver desvantagem.

    Args:
        personagem (dict): Dicionário contendo os dados do personagem (nome, forca, elemento).
        oponentes (list): Lista de dicionários, cada um representando um personagem oponente.

    Returns:
        int: A força do personagem ajustada.
    """
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    # Calcula o número de vantagens: soma 1 para cada oponente cujo elemento está na lista de vantagens do personagem.
    vantagem = sum(1 for o in oponentes if o["elemento"] in VANTAGENS.get(elemento, []))
    # Calcula o número de desvantagens: soma 1 para cada oponente cujo elemento está na lista de desvantagens do personagem.
    desvantagem = sum(1 for o in oponentes if o["elemento"] in DESVANTAGENS.get(elemento, []))

    # Define os valores de bônus e penalidades (1000 por vantagem, 500 por desvantagem).
    bonus = 1000 * vantagem
    penalidade = 500 * desvantagem

    # Retorna a força inicial do personagem, aplicando o bônus e a penalidade.
    return forca + bonus - penalidade


def aplicar_cenario(personagem, cenario_nome):
    """
    Aplica modificadores de força a um personagem com base no cenário da batalha.
    Verifica se o elemento do personagem recebe bônus ou penalidade no cenário.

    Args:
        personagem (dict): Dicionário com os dados do personagem (nome, forca, elemento).
        cenario_nome (str): O nome do cenário atual da batalha.

    Returns:
        int: A força do personagem ajustada pelo cenário.
    """
    # Tenta obter os dados do cenário usando o nome (convertido para minúsculas).
    cenario = CENARIOS.get(cenario_nome.lower())
    # Se o cenário não for encontrado (nome inválido), retorna a força original do personagem.
    if not cenario:
        return personagem["forca"]
    
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    # Se o elemento do personagem estiver na lista de bônus do cenário, adiciona o valor de bônus à força.
    if elemento in cenario["bonus"]:
        forca += cenario["bonus_valor"]
    # Se o elemento do personagem estiver na lista de penalidades do cenário, subtrai o valor da penalidade da força.
    if elemento in cenario["penalidade"]:
        forca -= cenario["penalidade_valor"]

    # Retorna a força final após aplicar os modificadores do cenário.
    return forca