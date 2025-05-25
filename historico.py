import json # Usado para serializar (salvar) e deserializar (carregar) dados em formato JSON.
import os   # Usado para interagir com o sistema operacional, como verificar a existência de arquivos e criar diretórios.
# from datetime import datetime # Esta importação não está sendo usada no código fornecido.

# Define o diretório base do arquivo Python atual.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Constrói o caminho completo para o arquivo JSON que armazenará o histórico de batalhas.
# Ele será salvo em uma subpasta 'data' dentro do diretório base.
ARQUIVO_HISTORICO = os.path.join(BASE_DIR, 'data', 'historico_batalhas.json')

historico = [] # Lista global para armazenar o histórico de batalhas em memória durante a execução.

def carregar_historico():
    """
    Carrega o histórico de batalhas do arquivo JSON para a memória.
    Retorna uma lista com os registros de batalhas.
    Se o arquivo não existir ou estiver vazio, retorna uma lista vazia.
    """
    # Verifica se o arquivo de histórico existe no caminho especificado.
    if os.path.exists(ARQUIVO_HISTORICO):
        # Verifica se o tamanho do arquivo é maior que 0 para evitar erros de JSON vazio.
        if os.path.getsize(ARQUIVO_HISTORICO) > 0:
            # Abre o arquivo no modo de leitura ('r') com codificação UTF-8.
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                # Carrega o conteúdo JSON do arquivo e o retorna.
                return json.load(f)
        else:
            # Se o arquivo estiver vazio, retorna uma lista vazia.
            return []
    # Se o arquivo não existir, retorna uma lista vazia.
    return []

def salvar_historico(historico):
    """
    Salva o histórico de batalhas atual (passado como argumento) no arquivo JSON.

    Args:
        historico (list): A lista de dicionários contendo os registros das batalhas.
    """
    # Abre o arquivo no modo de escrita ('w') com codificação UTF-8.
    # json.dump serializa a lista 'historico' para JSON e a escreve no arquivo.
    # indent=4 formata o JSON com indentação para melhor legibilidade.
    # ensure_ascii=False permite que caracteres não-ASCII (como acentos) sejam gravados diretamente.
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

def registrar_batalha(time1, time2, vencedor):
    """
    Adiciona um novo registro de batalha ao histórico e o salva no arquivo.

    Args:
        time1 (str): O nome do primeiro time participante.
        time2 (str): O nome do segundo time participante.
        vencedor (str): O nome do time vencedor ou "Empate" em caso de empate.
    """
    # Carrega o histórico existente para adicionar o novo registro.
    historico = carregar_historico()
    # Cria um dicionário para o novo registro da batalha.
    registro = {
        'time1': time1,
        'time2': time2,
        'vencedor': vencedor,
    }
    # Adiciona o novo registro à lista do histórico.
    historico.append(registro)
    # Salva a lista atualizada de volta no arquivo.
    salvar_historico(historico)

def exibir_historico():
    """
    Carrega e exibe todos os registros de batalhas presentes no histórico.
    Se não houver batalhas registradas, exibe uma mensagem apropriada.
    """
    # Carrega o histórico para exibição.
    historico = carregar_historico()
    # Verifica se o histórico está vazio.
    if not historico:
        print("Nenhuma batalha registrada.")
        return

    print("\n=== HISTÓRICO DE BATALHAS ===")
    # Itera sobre cada batalha no histórico e exibe seus detalhes formatados.
    # enumerate(historico, 1) começa a contagem a partir de 1.
    for idx, batalha in enumerate(historico, 1):
        print(f"{idx}. {batalha['time1']} vs {batalha['time2']} - Vencedor: {batalha['vencedor']}")