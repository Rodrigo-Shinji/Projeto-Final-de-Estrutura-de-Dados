import json # Usado para serializar (salvar) e deserializar (carregar) dados em formato JSON.
import os   # Usado para interagir com o sistema operacional (caminhos de arquivo, diretórios).

# Importa a classe ListaEncadeada personalizada para gerenciar os personagens dentro de cada time.
from lista_encadeada import ListaEncadeada
# Importa funções do módulo 'personagem' para obter e listar personagens.
# 'personagens' (o dicionário global de todos os personagens) também é importado para referência.
from personagem import obter_personagem, listar_personagens, personagens

# Define o diretório base do arquivo Python atual.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Constrói o caminho completo para o arquivo JSON que armazenará os dados dos times.
# O arquivo ficará na pasta 'data' dentro do diretório base do projeto.
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "data", "times.json")

# Dicionário global 'times': Armazena todos os times em memória.
# A chave é o nome do time (string) e o valor é uma instância de ListaEncadeada,
# que contém os objetos de personagens associados a esse time.
times = {}

def carregar_times():
    """
    Carrega os dados dos times do arquivo JSON para o dicionário global 'times' em memória.
    Cada lista de personagens dentro de um time é reconstruída como uma ListaEncadeada
    para manter a estrutura de dados original.
    Trata casos onde o arquivo não existe ou está corrompido (JSON inválido).
    """
    global times # Declara que estamos modificando a variável global 'times'.
    # Verifica se o arquivo de times existe no caminho especificado.
    if os.path.exists(CAMINHO_ARQUIVO):
        try:
            # Abre o arquivo no modo de leitura ('r') com codificação UTF-8.
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f) # Carrega o conteúdo JSON (que é um dicionário de listas de personagens).
                times.clear() # Limpa o dicionário 'times' atual para carregar os novos dados.
                # Itera sobre os dados carregados: para cada nome de time e sua lista de personagens,
                # cria uma nova ListaEncadeada a partir da lista e a adiciona ao dicionário 'times'.
                # Isso reconstrói as ListasEncadeadas a partir dos dados persistidos.
                times.update({
                    nome_time: ListaEncadeada.from_list(lista) for nome_time, lista in dados.items()
                })
            print("Times carregados do arquivo.")
        except FileNotFoundError: # Captura erro se o arquivo não for encontrado durante a abertura.
            print(f"Arquivo de times não encontrado em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times.clear() # Reseta 'times' para um dicionário vazio.
        except json.JSONDecodeError: # Captura erro se o JSON no arquivo estiver malformado.
            print(f"Erro ao decodificar JSON do arquivo de times em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
            times.clear() # Reseta 'times' para um dicionário vazio.
    else: # Se o arquivo de times não existir no caminho especificado.
        print(f"Arquivo de times não existe em: {CAMINHO_ARQUIVO}. Iniciando com times vazios.")
        times.clear() # Inicializa 'times' como um dicionário vazio.

def salvar_times():
    """
    Salva os dados atuais do dicionário 'times' (em memória) para o arquivo JSON.
    Antes de salvar, converte cada ListaEncadeada de personagens de volta para uma
    lista Python comum, pois a ListaEncadeada não é diretamente serializável por JSON.
    Cria o diretório 'data' se ele não existir.
    """
    # Garante que o diretório onde o arquivo será salvo ('data') exista.
    # `exist_ok=True` evita um erro se o diretório já existir.
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    # Prepara os dados para serialização: Para cada time, obtém a lista de dicionários
    # de personagens da ListaEncadeada usando o método `.listar()`.
    serializado = {
        nome_time: lista.listar() for nome_time, lista in times.items()
    }
    try:
        # Abre o arquivo no modo de escrita ('w') com codificação UTF-8.
        # `json.dump` serializa o dicionário `serializado` para JSON.
        # `indent=2` formata o JSON com indentação de 2 espaços para melhor legibilidade.
        # `ensure_ascii=False` permite que caracteres não-ASCII (como acentos) sejam gravados diretamente.
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(serializado, f, indent=2, ensure_ascii=False)
        print("Times salvos no arquivo.")
    except IOError: # Captura erros de entrada/saída que podem ocorrer durante a escrita do arquivo.
        print(f"Erro ao salvar os times no arquivo: {CAMINHO_ARQUIVO}.")

def criar_time(nome_time):
    """
    Cria um novo time com o nome fornecido, se ele ainda não existir.

    Args:
        nome_time (str): O nome do time a ser criado.

    Returns:
        bool: True se o time foi criado com sucesso, False se já existia.
    """
    nome_time_strip = nome_time.strip() # Remove espaços extras do nome de entrada.
    if nome_time_strip in times: # Verifica se o time com o nome normalizado já existe no dicionário global 'times'.
        print(f"O time '{nome_time_strip}' já existe.")
        return False
    # Cria uma nova instância de ListaEncadeada (vazia) para o novo time
    # e a adiciona ao dicionário 'times' com o nome normalizado como chave.
    times[nome_time_strip] = ListaEncadeada()
    salvar_times() # Salva a alteração (novo time) no arquivo de persistência.
    print(f"Time '{nome_time_strip}' criado.")
    return True

def excluir_time(nome_time):
    """
    Remove um time existente pelo nome.

    Args:
        nome_time (str): O nome do time a ser excluído.

    Returns:
        bool: True se o time foi excluído com sucesso, False se não foi encontrado.
    """
    nome_time_strip = nome_time.strip() # Remove espaços extras do nome de entrada.
    if nome_time_strip in times: # Verifica se o time com o nome normalizado existe.
        del times[nome_time_strip] # Remove a entrada do time do dicionário 'times'.
        salvar_times() # Salva a alteração (time excluído) no arquivo de persistência.
        print(f"Time '{nome_time_strip}' excluído.")
        return True
    print(f"Time '{nome_time_strip}' não encontrado.") # Mensagem se o time não for encontrado.
    return False

def mostrar_personagens_disponiveis():
    """
    Lista todos os personagens cadastrados no sistema.
    Esta função simplesmente chama 'listar_personagens' do módulo 'personagem',
    que já imprime e retorna a lista de personagens.
    É útil para o usuário ver quais personagens podem ser adicionados a um time.
    """
    # Chama a função do módulo 'personagem' para listar e exibir todos os personagens.
    personagens_existentes = listar_personagens()
    if not personagens_existentes: # Se a lista de personagens estiver vazia.
        print("Nenhum personagem criado ainda.")
        return

def adicionar_personagem_ao_time(nome_time, nome_personagem):
    """
    Adiciona um personagem a um time específico.
    Realiza várias validações:
    1. Existência do time.
    2. Existência do personagem.
    3. Se o personagem já pertence a *qualquer* outro time.
    4. Se o time já atingiu o limite máximo de 4 personagens.

    Args:
        nome_time (str): O nome do time ao qual adicionar o personagem.
        nome_personagem (str): O nome do personagem a ser adicionado.

    Returns:
        bool: True se o personagem foi adicionado com sucesso, False caso contrário.
    """
    nome_time_strip = nome_time.strip()       # Normaliza o nome do time.
    nome_personagem_strip = nome_personagem.strip() # Normaliza o nome do personagem.

    if nome_time_strip not in times: # Validação 1: Verifica se o time existe.
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False

    personagem = obter_personagem(nome_personagem_strip) # Validação 2: Tenta obter os dados do personagem.
    if not personagem: # Verifica se o personagem existe no cadastro geral.
        print(f"Personagem '{nome_personagem_strip}' não encontrado.")
        return False

    # Validação 3: Itera sobre todos os times para verificar se o personagem já está em algum.
    for time_nome, lista in times.items():
        if lista.contem(nome_personagem_strip): # Usa o método 'contem' da ListaEncadeada para verificar a presença.
            print(f"Personagem '{nome_personagem_strip}' já pertence ao time '{time_nome}'.")
            return False

    # Validação 4: Verifica o limite de 4 personagens por time.
    time_alvo = times[nome_time_strip] # Obtém a instância de ListaEncadeada do time alvo.
    if len(time_alvo.listar()) >= 4: # Usa o método .listar() da ListaEncadeada para obter a contagem atual.
        print(f"O time '{nome_time_strip}' já atingiu o limite máximo de 4 personagens.")
        return False

    # Se todas as validações passarem, insere o personagem na ListaEncadeada do time alvo.
    time_alvo.inserir(personagem)
    salvar_times() # Salva a alteração no arquivo de persistência.
    print(f"Personagem '{nome_personagem_strip}' adicionado ao time '{nome_time_strip}'.")
    return True

def remover_personagem_do_time(nome_time, nome_personagem):
    """
    Remove um personagem de um time específico.

    Args:
        nome_time (str): O nome do time do qual remover o personagem.
        nome_personagem (str): O nome do personagem a ser removido.

    Returns:
        bool: True se o personagem foi removido com sucesso, False caso contrário.
    """
    nome_time_strip = nome_time.strip()       # Normaliza o nome do time.
    nome_personagem_strip = nome_personagem.strip() # Normaliza o nome do personagem.

    if nome_time_strip not in times: # Verifica se o time existe.
        print(f"Time '{nome_time_strip}' não encontrado.")
        return False

    # Tenta remover o personagem da ListaEncadeada do time usando o método 'remover'.
    if times[nome_time_strip].remover(nome_personagem_strip):
        salvar_times() # Salva a alteração no arquivo de persistência.
        print(f"Personagem '{nome_personagem_strip}' removido do time '{nome_time_strip}'.")
        return True
    else:
        print(f"Personagem '{nome_personagem_strip}' não encontrado no time '{nome_time_strip}'.")
        return False

def listar_times():
    """
    Lista todos os times cadastrados e os personagens que pertencem a cada um.
    Retorna uma lista contendo os nomes dos times.
    """
    if not times: # Verifica se há times cadastrados no dicionário global 'times'.
        print("Nenhum time cadastrado.")
        return [] # Retorna uma lista vazia se não houver times.

    print("\n=== LISTA DE TIMES ===")
    lista_nomes = [] # Lista para armazenar e retornar os nomes dos times.
    # Itera sobre cada item (nome do time e sua ListaEncadeada de personagens) no dicionário 'times'.
    for nome_time, lista_personagens in times.items():
        personagens_no_time = lista_personagens.listar() # Obtém a lista de dicionários de personagens do time.
        # Extrai apenas os nomes dos personagens para exibição mais limpa.
        nomes_personagens = [p['nome'] for p in personagens_no_time]
        # Imprime o nome do time e seus personagens. Se o time estiver vazio, indica "(Vazio)".
        print(f"- {nome_time}: {', '.join(nomes_personagens) if nomes_personagens else '(Vazio)'}")
        lista_nomes.append(nome_time) # Adiciona o nome do time à lista para retorno.
    return lista_nomes # Retorna a lista de nomes de times.

def listar_nomes_dos_times():
    """
    Retorna uma lista contendo apenas os nomes (chaves) de todos os times cadastrados.

    Returns:
        list: Uma lista de strings com os nomes dos times.
    """
    return list(times.keys()) # Retorna as chaves do dicionário 'times' convertidas para uma lista.

def obter_forca_total_time(nome_time):
    """
    Calcula e retorna a força total de um time específico somando a força de todos os seus personagens.

    Args:
        nome_time (str): O nome do time cuja força total será calculada.

    Returns:
        int: A força total do time, ou 0 se o time não for encontrado.
    """
    nome_time_strip = nome_time.strip() # Normaliza o nome do time.
    if nome_time_strip in times: # Verifica se o time existe.
        # Chama o método `calcular_forca_total` da ListaEncadeada associada ao time para obter a soma das forças.
        return times[nome_time_strip].calcular_forca_total()
    return 0 # Retorna 0 se o time não for encontrado.

def obter_personagens_do_time(nome_time):
    """
    Retorna uma lista de dicionários de personagens pertencentes a um time específico.

    Args:
        nome_time (str): O nome do time.

    Returns:
        list: Uma lista de dicionários de personagens, ou uma lista vazia se o time não existir.
    """
    nome_time_strip = nome_time.strip() # Normaliza o nome do time.
    if nome_time_strip in times: # Verifica se o time existe.
        # Chama o método `listar` da ListaEncadeada para obter todos os personagens do time em formato de lista.
        return times[nome_time_strip].listar()
    return [] # Retorna uma lista vazia se o time não for encontrado.

def listar_personagens_do_time(nome_time):
    """
    Imprime na tela os personagens de um time específico, mostrando seus detalhes.

    Args:
        nome_time (str): O nome do time cujos personagens serão listados.
    """
    nome_time_strip = nome_time.strip() # Normaliza o nome do time.
    if nome_time_strip not in times: # Verifica se o time existe.
        print(f"Time '{nome_time_strip}' não encontrado.")
        return

    personagens_do_time = times[nome_time_strip].listar() # Obtém a lista de personagens do time.
    if not personagens_do_time: # Verifica se o time possui personagens.
        print(f"O time '{nome_time_strip}' não possui personagens.")
        return

    print(f"\n=== PERSONAGENS DO TIME '{nome_time_strip}' ===")
    # Itera e imprime os detalhes (nome, força, elemento) de cada personagem do time.
    for p in personagens_do_time:
        print(f"- {p['nome']} (Força: {p['forca']}, Elemento: {p['elemento']})")