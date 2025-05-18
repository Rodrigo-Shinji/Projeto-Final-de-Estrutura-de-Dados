from time import sleep  # Importa a função sleep para criar pausas entre as mensagens
from times import (
    obter_forca_total_time,  # Calcula a força total de um time
    carregar_times,          # Carrega os dados dos times salvos
    obter_personagens_do_time,  # Retorna os personagens de um time específico
    listar_nomes_dos_times   # Lista todos os nomes dos times cadastrados
)
from historico import registrar_batalha
# Carrega os times do arquivo para garantir que os dados estejam atualizados
carregar_times()

# Função auxiliar que verifica se um time existe (desconsidera maiúsculas/minúsculas e espaços extras)
def time_existe_normalizado(nome_time):
    nome_normalizado = nome_time.strip().lower()  # Remove espaços e converte para minúsculas
    return any(nome_normalizado == nome.strip().lower() for nome in listar_nomes_dos_times())

# Função principal que realiza a batalha entre dois times
def batalhar(nome_time1: str, nome_time2: str) -> None:
    carregar_times()  # Recarrega os dados para garantir atualizações recentes
    erros = []

    # Verifica se os times informados existem
    if not time_existe_normalizado(nome_time1):
        erros.append(f"Time '{nome_time1}' não existe.")
    if not time_existe_normalizado(nome_time2):
        erros.append(f"Time '{nome_time2}' não existe.")

    # Se houver erros, exibe e encerra a batalha
    if erros:
        print("\n".join(erros))
        return

    # Obtém os personagens de cada time
    personagens1 = obter_personagens_do_time(nome_time1)
    personagens2 = obter_personagens_do_time(nome_time2)

    # Verifica se os dois times possuem ao menos um personagem
    if not personagens1:
        print(f"O time '{nome_time1}' não possui personagens para batalhar. Selecione outro time.")
        return
    if not personagens2:
        print(f"O time '{nome_time2}' não possui personagens para batalhar. Selecione outro time.")
        return

    # Mensagens de introdução da batalha com pausas para melhorar a apresentação
    print(f"\nA batalha épica está prestes a começar entre '{nome_time1}' e '{nome_time2}'!")
    sleep(1.5)
    print("Os guerreiros entram em campo...")
    sleep(1.5)

    # Apresenta os personagens do primeiro time
    print(f"\nLutadores do time '{nome_time1}':")
    for p in personagens1:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5)

    # Apresenta os personagens do segundo time
    print(f"\nLutadores do time '{nome_time2}':")
    for p in personagens2:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5)

    # Mensagem de início da batalha
    sleep(1)
    print("\nA batalha começa!")
    sleep(2)

    # Calcula a força total de cada time
    forca1 = obter_forca_total_time(nome_time1)
    forca2 = obter_forca_total_time(nome_time2)

    # Exibe os totais de força dos dois times
    print(f"\n{nome_time1} acumulou {forca1} pontos de força.")
    sleep(1)
    print(f"{nome_time2} acumulou {forca2} pontos de força.")
    sleep(1.5)

# Determina e exibe o vencedor (ou empate)
    if forca1 > forca2:
        print(f"\nApós uma luta intensa, o time '{nome_time1}' triunfa com glória!")
        vencedor = nome_time1
    elif forca2 > forca1:
        print(f"\n'{nome_time2}' domina o campo e conquista a vitória!")
        vencedor = nome_time2
    else:
        print("\nÉ um empate! Ambos os times lutaram com bravura.")
        vencedor = "Empate"

    # Registra o resultado da batalha
    registrar_batalha(nome_time1, nome_time2, vencedor)

    print("Fim da batalha.\n")
