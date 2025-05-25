# Importa a função sleep para criar pausas na execução e melhorar a experiência do usuário.
from time import sleep

# Importa a função registrar_batalha para salvar o resultado de cada confronto no histórico.
from historico import registrar_batalha
# Importa obter_personagem para buscar detalhes de um personagem específico.
from personagem import obter_personagem
# Importa as definições de vantagens, desvantagens e cenários para aplicar modificadores na batalha.
from elementos import VANTAGENS, DESVANTAGENS, CENARIOS
# Importa funções e o dicionário 'times' do módulo 'times' para gerenciar informações dos times.
from times import (
    carregar_times,           # Recarrega os dados dos times do arquivo.
    listar_nomes_dos_times,   # Obtém uma lista com os nomes de todos os times.
    obter_personagens_do_time,# Obtém a lista de personagens de um time específico.
    times                     # O dicionário global que armazena os times em memória.
)

# Carrega os dados dos times assim que o módulo é importado, garantindo que estejam atualizados.
carregar_times()

def time_existe_normalizado(nome_time):
    """
    Verifica se um time existe na lista de times cadastrados, ignorando
    diferenças entre maiúsculas/minúsculas e espaços em branco extras.
    Normaliza o nome de entrada e compara com os nomes normalizados dos times existentes.
    """
    nome_normalizado = nome_time.strip().lower() # Remove espaços extras e converte para minúsculas
    # Retorna True se encontrar qualquer time cujo nome normalizado corresponda ao nome de entrada normalizado.
    return any(nome_normalizado == nome.strip().lower() for nome in listar_nomes_dos_times())

def ajustar_forca_com_elementos(personagem, oponentes):
    """
    Calcula o ajuste na força de um personagem com base nas vantagens e desvantagens elementais
    contra os elementos dos personagens oponentes.

    Args:
        personagem (dict): Dicionário contendo os dados do personagem (nome, forca, elemento).
        oponentes (list): Lista de dicionários, cada um representando um personagem oponente.

    Returns:
        int: A força do personagem ajustada pelos bônus e penalidades elementais.
    """
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    # Conta quantas vantagens o personagem tem contra os elementos dos oponentes.
    vantagem = sum(1 for o in oponentes if o["elemento"] in VANTAGENS.get(elemento, []))
    # Conta quantas desvantagens o personagem tem contra os elementos dos oponentes.
    desvantagem = sum(1 for o in oponentes if o["elemento"] in DESVANTAGENS.get(elemento, []))

    # Calcula o bônus total (1000 por vantagem).
    bonus = 1000 * vantagem
    # Calcula a penalidade total (500 por desvantagem).
    penalidade = 500 * desvantagem

    # Retorna a força base mais o bônus e menos a penalidade.
    return forca + bonus - penalidade

def aplicar_cenario(personagem, cenario_nome):
    """
    Aplica modificadores de força a um personagem com base no cenário da batalha.
    Personagens com elementos bônus no cenário recebem um aumento de força,
    enquanto aqueles com elementos de penalidade sofrem uma redução.

    Args:
        personagem (dict): Dicionário com os dados do personagem (nome, forca, elemento).
        cenario_nome (str): O nome do cenário atual da batalha.

    Returns:
        int: A força do personagem ajustada pelo cenário.
    """
    # Busca o cenário pelo nome (convertendo para minúsculas para corresponder à chave).
    cenario = CENARIOS.get(cenario_nome.lower())
    # Se o cenário não for encontrado, retorna a força original do personagem.
    if not cenario:
        return personagem["forca"]

    elemento = personagem["elemento"]
    forca = personagem["forca"]

    # Se o elemento do personagem estiver na lista de bônus do cenário, adiciona o valor do bônus.
    if elemento in cenario["bonus"]:
        forca += cenario["bonus_valor"]
    # Se o elemento do personagem estiver na lista de penalidades do cenário, subtrai o valor da penalidade.
    if elemento in cenario["penalidade"]:
        forca -= cenario["penalidade_valor"]

    # Retorna a força ajustada pelo cenário.
    return forca

def calcular_forca_total_ajustada(nome_time, nome_time_inimigo, cenario_nome):
    """
    Calcula a força total ajustada de um time, considerando as vantagens/desvantagens elementais
    de seus personagens contra o time inimigo e os modificadores do cenário.

    Args:
        nome_time (str): O nome do time cuja força total será calculada.
        nome_time_inimigo (str): O nome do time oponente.
        cenario_nome (str): O nome do cenário da batalha.

    Returns:
        int: A força total ajustada do time.
    """
    # Obtém os personagens do time atual e do time inimigo.
    personagens = obter_personagens_do_time(nome_time)
    oponentes = obter_personagens_do_time(nome_time_inimigo)
    total = 0
    # Itera sobre cada personagem do time atual.
    for p in personagens:
        # Obtém os dados completos do personagem a partir do módulo 'personagem'.
        p_completo = obter_personagem(p["nome"])
        if p_completo:
            # Garante que o elemento do personagem (que vem do time) está nos dados completos.
            p_completo["elemento"] = p["elemento"]
            # Calcula a força base ajustada pelas vantagens/desvantagens elementais.
            base = ajustar_forca_com_elementos(p_completo, oponentes)
            # Aplica os modificadores do cenário à força base.
            final = aplicar_cenario(p_completo, cenario_nome)
            # Acumula a força final do personagem ao total do time.
            total += final
    return total

def batalhar(nome_time1: str, nome_time2: str, cenario) -> None:
    """
    Simula uma batalha entre dois times, calculando suas forças ajustadas
    com base em elementos e cenário, e determinando um vencedor.
    O resultado da batalha é registrado no histórico.

    Args:
        nome_time1 (str): O nome do primeiro time participante da batalha.
        nome_time2 (str): O nome do segundo time participante da batalha.
        cenario (str): O nome do cenário onde a batalha ocorrerá.
    """
    # Recarrega os dados dos times para garantir que quaisquer alterações recentes sejam consideradas.
    carregar_times()

    erros = [] # Lista para armazenar mensagens de erro caso os times não existam.

    # Verifica se o primeiro time existe.
    if not time_existe_normalizado(nome_time1):
        erros.append(f"Time '{nome_time1}' não existe.")
    # Verifica se o segundo time existe.
    if not time_existe_normalizado(nome_time2):
        erros.append(f"Time '{nome_time2}' não existe.")

    # Se houver erros (times não encontrados), exibe as mensagens e encerra a função.
    if erros:
        print("\n".join(erros))
        return

    # Obtém a lista de personagens para cada time.
    personagens1 = obter_personagens_do_time(nome_time1)
    personagens2 = obter_personagens_do_time(nome_time2)

    # Verifica se o primeiro time possui personagens.
    if not personagens1:
        print(f"O time '{nome_time1}' não possui personagens para batalhar. Selecione outro time.")
        return
    # Verifica se o segundo time possui personagens.
    if not personagens2:
        print(f"O time '{nome_time2}' não possui personagens para batalhar. Selecione outro time.")
        return
    
    # Exibe o cenário escolhido.
    print(f"Cenário escolhido: {cenario.title()}")

    # Mensagens de introdução à batalha, com pausas para um efeito dramático.
    print(f"\nA batalha épica está prestes a começar entre '{nome_time1}' e '{nome_time2}'!")
    sleep(1.5)
    print("Os guerreiros entram em campo...")
    sleep(1.5)

    # Lista os personagens do primeiro time.
    print(f"\nLutadores do time '{nome_time1}':")
    for p in personagens1:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5) # Pequena pausa para cada personagem listado.

    # Lista os personagens do segundo time.
    print(f"\nLutadores do time '{nome_time2}':")
    for p in personagens2:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5)

    # Mensagem de início da batalha.
    sleep(1)
    print("\nA batalha começa!")
    sleep(2)

    # Calcula a força total ajustada para cada time, considerando o time inimigo e o cenário.
    forca1 = calcular_forca_total_ajustada(nome_time1, nome_time2, cenario)
    forca2 = calcular_forca_total_ajustada(nome_time2, nome_time1, cenario)

    # Exibe a força total de cada time.
    print(f"\n{nome_time1} acumulou {forca1} pontos de força.")
    sleep(1)
    print(f"{nome_time2} acumulou {forca2} pontos de força.")
    sleep(1.5)

    # Determina o vencedor da batalha com base nas forças totais.
    if forca1 > forca2:
        print(f"\nApós uma luta intensa, o time '{nome_time1}' triunfa com glória!")
        vencedor = nome_time1
    elif forca2 > forca1:
        print(f"\n'{nome_time2}' domina o campo e conquista a vitória!")
        vencedor = nome_time2
    else:
        print("\nÉ um empate! Ambos os times lutaram com bravura.")
        vencedor = "Empate"

    # Registra o resultado da batalha no histórico.
    registrar_batalha(nome_time1, nome_time2, vencedor)

    print("Fim da batalha.\n")