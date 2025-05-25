from time import sleep

from historico import registrar_batalha
from personagem import obter_personagem
from elementos import VANTAGENS, DESVANTAGENS, CENARIOS
from times import (
    carregar_times,
    listar_nomes_dos_times,
    obter_personagens_do_time,
    times
)

def time_existe_normalizado(nome_time):
    nome_normalizado = nome_time.strip().lower()
    return any(nome_normalizado == nome.strip().lower() for nome in listar_nomes_dos_times())

def ajustar_forca_com_elementos(personagem, oponentes):
    elemento = personagem["elemento"]
    forca = personagem["forca"]

    vantagem = sum(1 for o in oponentes if o["elemento"] in VANTAGENS.get(elemento, []))
    desvantagem = sum(1 for o in oponentes if o["elemento"] in DESVANTAGENS.get(elemento, []))

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

def calcular_forca_total_ajustada(nome_time, nome_time_inimigo, cenario_nome):
    personagens = obter_personagens_do_time(nome_time)
    oponentes = obter_personagens_do_time(nome_time_inimigo)
    total = 0
    for p in personagens:
        p_completo = obter_personagem(p["nome"])
        if p_completo:
            p_completo["elemento"] = p["elemento"]
            base = ajustar_forca_com_elementos(p_completo, oponentes)
            final = aplicar_cenario(p_completo, cenario_nome)
            total += final
    return total

def batalhar(nome_time1: str, nome_time2: str, cenario) -> None:
    carregar_times()

    erros = []

    if not time_existe_normalizado(nome_time1):
        erros.append(f"Time '{nome_time1}' não existe.")
    if not time_existe_normalizado(nome_time2):
        erros.append(f"Time '{nome_time2}' não existe.")

    if erros:
        print("\n".join(erros))
        return

    personagens1 = obter_personagens_do_time(nome_time1)
    personagens2 = obter_personagens_do_time(nome_time2)

    if not personagens1:
        print(f"O time '{nome_time1}' não possui personagens para batalhar. Selecione outro time.")
        return
    if not personagens2:
        print(f"O time '{nome_time2}' não possui personagens para batalhar. Selecione outro time.")
        return
    
    print(f"Cenário escolhido: {cenario.title()}")

    print(f"\nA batalha épica está prestes a começar entre '{nome_time1}' e '{nome_time2}'!")
    sleep(1.5)
    print("Os guerreiros entram em campo...")
    sleep(1.5)

    print(f"\nLutadores do time '{nome_time1}':")
    for p in personagens1:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5)

    print(f"\nLutadores do time '{nome_time2}':")
    for p in personagens2:
        print(f"{p['nome']} (Força: {p['forca']})")
        sleep(0.5)

    sleep(1)
    print("\nA batalha começa!")
    sleep(2)

    forca1 = calcular_forca_total_ajustada(nome_time1, nome_time2, cenario)
    forca2 = calcular_forca_total_ajustada(nome_time2, nome_time1, cenario)

    print(f"\n{nome_time1} acumulou {forca1} pontos de força.")
    sleep(1)
    print(f"{nome_time2} acumulou {forca2} pontos de força.")
    sleep(1.5)

    if forca1 > forca2:
        print(f"\nApós uma luta intensa, o time '{nome_time1}' triunfa com glória!")
        vencedor = nome_time1
    elif forca2 > forca1:
        print(f"\n'{nome_time2}' domina o campo e conquista a vitória!")
        vencedor = nome_time2
    else:
        print("\nÉ um empate! Ambos os times lutaram com bravura.")
        vencedor = "Empate"

    registrar_batalha(nome_time1, nome_time2, vencedor)

    print("Fim da batalha.\n")