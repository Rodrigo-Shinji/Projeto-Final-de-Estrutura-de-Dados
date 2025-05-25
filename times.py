import json
import os

from lista_encadeada import ListaEncadeada
from personagem import obter_personagem, listar_personagens, personagens

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "data", "times.json")

times = {}

def carregar_times():
    global times
    if os.path.exists(CAMINHO_ARQUIVO):
        try:
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                times.clear()
                times.update({
                    nome_time: ListaEncadeada.from_list(lista) for nome_time, lista in dados.items()
                })
            print("Times carregados do arquivo.")
        except FileNotFoundError:
            print(f"Arquivo de times não encontrado em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times.clear()
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON do arquivo de times em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times.clear()
    else:
        print(f"Arquivo de times não existe em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
        times.clear()

def salvar_times():
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    serializado = {
        nome_time: lista.listar() for nome_time, lista in times.items()
    }
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(serializado, f, indent=2, ensure_ascii=False)
        print("Times salvos no arquivo.")
    except IOError:
        print(f"Erro ao salvar os times no arquivo: {CAMINHO_ARQUIVO}.")

def criar_time(nome_time):
    if nome_time.strip() in times:
        print(f"O time '{nome_time.strip()}' já existe.")
        return False
    times[nome_time.strip()] = ListaEncadeada()
    salvar_times()
    print(f"Time '{nome_time.strip()}' criado.")
    return True

def excluir_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip in times:
        del times[nome_time_strip]
        salvar_times()
        print(f"Time '{nome_time_strip}' excluído.")
        return True
    print(f"Time '{nome_time_strip}' não encontrado.")
    return False

def mostrar_personagens_disponiveis():
    personagens = listar_personagens()
    if not personagens:
        print("Nenhum personagem criado ainda.")
        return

def adicionar_personagem_ao_time(nome_time, nome_personagem):
    nome_time_strip = nome_time.strip()
    nome_personagem_strip = nome_personagem.strip()

    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False

    personagem = obter_personagem(nome_personagem_strip)
    if not personagem:
        print(f"Personagem '{nome_personagem_strip}' não encontrado.")
        return False

    for time_nome, lista in times.items():
        if lista.contem(nome_personagem_strip):
            print(f"Personagem '{nome_personagem_strip}' já pertence ao time '{time_nome}'.")
            return False

    time_alvo = times[nome_time_strip]
    if len(time_alvo.listar()) >= 4:
        print(f"O time '{nome_time_strip}' já atingiu o limite máximo de 4 personagens.")
        return False

    time_alvo.inserir(personagem)
    salvar_times()
    print(f"Personagem '{nome_personagem_strip}' adicionado ao time '{nome_time_strip}'.")
    return True

def remover_personagem_do_time(nome_time, nome_personagem):
    nome_time_strip = nome_time.strip()
    nome_personagem_strip = nome_personagem.strip()

    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False

    if times[nome_time_strip].remover(nome_personagem_strip):
        salvar_times()
        print(f"Personagem '{nome_personagem_strip}' removido do time '{nome_time_strip}'.")
        return True
    else:
        print(f"Personagem '{nome_personagem_strip}' não encontrado no time '{nome_time_strip}'.")
        return False

def listar_times():
    if not times:
        print("Nenhum time cadastrado.")
        return []
    print("\n=== LISTA DE TIMES ===")
    lista_nomes = []
    for nome_time, lista_personagens in times.items():
        personagens_no_time = lista_personagens.listar()
        nomes_personagens = [p['nome'] for p in personagens_no_time]
        print(f"- {nome_time}: {', '.join(nomes_personagens) if nomes_personagens else '(Vazio)'}")
        lista_nomes.append(nome_time)
    return lista_nomes

def listar_nomes_dos_times():
    return list(times.keys())

def obter_forca_total_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip in times:
        return times[nome_time_strip].calcular_forca_total()
    return 0

def obter_personagens_do_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip in times:
        return times[nome_time_strip].listar()
    return []

def listar_personagens_do_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return

    personagens_do_time = times[nome_time_strip].listar()
    if not personagens_do_time:
        print(f"O time '{nome_time_strip}' não possui personagens.")
        return

    print(f"\n=== PERSONAGENS DO TIME '{nome_time_strip}' ===")
    for p in personagens_do_time:
        print(f"- {p['nome']} (Força: {p['forca']}, Elemento: {p['elemento']})")