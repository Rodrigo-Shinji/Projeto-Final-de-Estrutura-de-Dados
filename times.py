from lista_encadeada import ListaEncadeada  # Importa a estrutura lista encadeada personalizada
from personagem import obter_personagem, listar_personagens  # Funções para obter personagens
import json
import os

# Define o diretório base do arquivo atual e o caminho para o arquivo JSON que armazena os times
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "data", "times.json")

# Dicionário global que armazenará os times, onde:
# chave = nome do time (string)
# valor = ListaEncadeada com personagens daquele time
times = {}

# Função que carrega os times do arquivo JSON para a variável global 'times'
def carregar_times():
    global times  # Usa a variável global
    if os.path.exists(CAMINHO_ARQUIVO):  # Verifica se o arquivo existe
        try:
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f)  # Lê o conteúdo JSON (dicionário com listas)
                # Para cada time, converte a lista simples em ListaEncadeada
                times = {
                    nome_time: ListaEncadeada.from_list(lista) for nome_time, lista in dados.items()
                }
            print("Times carregados do arquivo.")
        except FileNotFoundError:
            # Caso o arquivo não seja encontrado (raro, pois já verificamos a existência)
            print(f"Arquivo de times não encontrado em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times = {}
        except json.JSONDecodeError:
            # Se o arquivo existe mas está corrompido ou inválido
            print(f"Erro ao decodificar JSON do arquivo de times em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times = {}
    else:
        # Arquivo não existe - inicia com times vazios
        print(f"ℹ️ Arquivo de times não existe em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
        times = {}

# Função para salvar os dados atuais dos times no arquivo JSON
def salvar_times():
    # Garante que o diretório do arquivo existe (cria caso não exista)
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    # Prepara os dados para salvar, convertendo cada ListaEncadeada em lista comum
    serializado = {
        nome_time: lista.listar() for nome_time, lista in times.items()
    }
    try:
        # Escreve os dados convertidos no arquivo JSON
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(serializado, f, indent=2, ensure_ascii=False)
        print("Times salvos no arquivo.")
    except IOError:
        print(f"Erro ao salvar os times no arquivo: {CAMINHO_ARQUIVO}.")

# Cria um novo time, caso ele ainda não exista
def criar_time(nome_time):
    if nome_time.strip() in times:
        print(f"O time '{nome_time.strip()}' já existe.")
        return False
    # Cria um novo time com lista vazia (ListaEncadeada)
    times[nome_time.strip()] = ListaEncadeada()
    salvar_times()
    print(f"Time '{nome_time.strip()}' criado.")
    return True

# Remove um time pelo nome, caso exista
def excluir_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip in times:
        del times[nome_time_strip]
        salvar_times()
        print(f"Time '{nome_time_strip}' excluído.")
        return True
    print(f"Time '{nome_time_strip}' não encontrado.")
    return False

from personagem import personagens  # acessa o dicionário diretamente

def mostrar_personagens_disponiveis():
    personagens = listar_personagens()  # <-- imprime e retorna
    if not personagens:
        print("Nenhum personagem criado ainda.")
        return
    print("\nPersonagens Criados:")
    for p in personagens:
        print(f"- {p['nome']} (Força: {p['forca']})")

# Adiciona um personagem a um time específico
def adicionar_personagem_ao_time(nome_time, nome_personagem):
    nome_time_strip = nome_time.strip()
    nome_personagem_strip = nome_personagem.strip()

    # Verifica se o time existe
    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False

    # Verifica se o personagem existe no cadastro geral
    personagem = obter_personagem(nome_personagem_strip)
    if not personagem:
        print(f"Personagem '{nome_personagem_strip}' não encontrado.")
        return False

    # Verifica se o personagem já pertence a algum time
    for time_nome, lista in times.items():
        if lista.contem(nome_personagem_strip):  # Método que verifica se o personagem está na lista
            print(f"Personagem '{nome_personagem_strip}' já pertence ao time '{time_nome}'.")
            return False

    # Insere o personagem na lista encadeada do time
    times[nome_time_strip].inserir(personagem)
    salvar_times()
    print(f"Personagem '{nome_personagem_strip}' adicionado ao time '{nome_time_strip}'.")
    return True

# Remove um personagem de um time, se estiver presente
def remover_personagem_do_time(nome_time, nome_personagem):
    nome_time_strip = nome_time.strip()
    nome_personagem_strip = nome_personagem.strip()
    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False
    sucesso = times[nome_time_strip].remover(nome_personagem_strip)  # Método para remover da lista encadeada
    if sucesso:
        salvar_times()
        print(f"Personagem '{nome_personagem_strip}' removido do time '{nome_time_strip}'.")
        return True
    print(f"Personagem '{nome_personagem_strip}' não está no time '{nome_time_strip}'.")
    return False

# Lista no console todos os times cadastrados
def listar_times():
    if not times:
        print("Nenhum time cadastrado.")
        return
    print("Lista de Times:")
    for nome in sorted(times.keys()):
        print(f"- {nome}")

# Lista os personagens de um time específico no console
def listar_personagens_do_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip not in times:
        print(f"Time '{nome_time_strip}' não encontrado.")
        return
    personagens = times[nome_time_strip].listar()  # Método que retorna uma lista comum dos personagens
    if not personagens:
        print(f"Nenhum personagem no time '{nome_time_strip}'.")
        return
    print(f"\nPersonagens no time '{nome_time_strip}':")
    for p in personagens:
        print(f"  - {p['nome']} (Força: {p['forca']})")

# Calcula a força total somando a força de todos os personagens de um time
def obter_forca_total_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip not in times:
        return 0
    # Método da lista encadeada para calcular a soma da força total
    return times[nome_time_strip].calcular_forca_total()

# Verifica se um time existe no dicionário de times
def time_existe(nome_time):
    return nome_time.strip() in times

# Retorna uma lista dos personagens de um time sem imprimir (útil para lógica interna)
def obter_personagens_do_time(nome_time):
    nome_time_strip = nome_time.strip()
    if nome_time_strip in times:
        return times[nome_time_strip].listar()
    return []

# Retorna uma lista com os nomes de todos os times cadastrados
def listar_nomes_dos_times():
    return list(times.keys())

# Quando o módulo é importado, os times são carregados automaticamente do arquivo JSON
carregar_times()