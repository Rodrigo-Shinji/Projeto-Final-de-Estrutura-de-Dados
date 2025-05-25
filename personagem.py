import json # Usado para serializar (salvar) e deserializar (carregar) dados em formato JSON.
import os   # Usado para interagir com o sistema operacional (caminhos de arquivo, diretórios).

# Dicionário global 'personagens': Armazena os dados de todos os personagens em memória.
# A chave é o nome do personagem (string) e o valor é um dicionário com seus atributos.
personagens = {}

# Define o diretório base onde este script está sendo executado.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Constrói o caminho completo para o arquivo JSON onde os personagens serão salvos/carregados.
# O arquivo ficará na pasta 'data' dentro do diretório base.
ARQUIVO = os.path.join(BASE_DIR, "data", "personagens.json")

# Conjunto 'ELEMENTOS_VALIDOS': Define os tipos de elementos que um personagem pode ter.
# Usar um 'set' é eficiente para verificações rápidas de pertinência (ex: 'elemento in ELEMENTOS_VALIDOS').
ELEMENTOS_VALIDOS = {"fogo", "terra", "luz", "trevas", "agua", "vento"}

def carregar_personagens():
    """
    Carrega os dados dos personagens do arquivo JSON para o dicionário 'personagens' em memória.
    Se o arquivo não existir ou for inválido (JSON malformado), inicializa 'personagens' como vazio.
    """
    global personagens # Declara que estamos modificando a variável global 'personagens'.
    # Verifica se o arquivo de personagens existe no caminho especificado.
    if os.path.exists(ARQUIVO):
        try:
            # Abre o arquivo no modo de leitura ('r') com codificação UTF-8.
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                personagens = json.load(f) # Carrega o conteúdo JSON para o dicionário.
        except json.JSONDecodeError: # Captura erro se o JSON no arquivo estiver malformado.
            print(f"Erro ao decodificar JSON do arquivo de personagens em: {ARQUIVO}. Iniciando com personagens vazios.")
            personagens = {} # Reseta personagens para um dicionário vazio.
    else:
        personagens = {} # Se o arquivo não existe, inicia com personagens vazios.

def salvar_personagens():
    """
    Salva os dados atuais do dicionário 'personagens' em memória para o arquivo JSON.
    Cria o diretório 'data' se ele não existir.
    """
    # Garante que o diretório onde o arquivo será salvo ('data') exista.
    # exist_ok=True evita um erro se o diretório já existir.
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    # Abre o arquivo no modo de escrita ('w') com codificação UTF-8.
    # json.dump serializa o dicionário 'personagens' para JSON.
    # indent=4 formata o JSON com indentação para melhor legibilidade.
    # ensure_ascii=False permite que caracteres não-ASCII (como acentos) sejam gravados diretamente.
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=4, ensure_ascii=False)

def cadastrar_personagem(nome, forca, elemento):
    """
    Cadastra um novo personagem no sistema.
    Verifica se o personagem já existe ou se o elemento é válido antes de adicionar.

    Args:
        nome (str): O nome do personagem.
        forca (int): O nível de força do personagem.
        elemento (str): O elemento do personagem (deve ser um dos ELEMENTOS_VALIDOS).
    """
    if nome in personagens: # Verifica se já existe um personagem com o mesmo nome.
        print("Personagem já existe.")
        return
    if elemento not in ELEMENTOS_VALIDOS: # Verifica se o elemento fornecido é válido.
        print(f"Elemento inválido. Escolha entre: {', '.join(sorted(list(ELEMENTOS_VALIDOS)))}")
        return

    # Adiciona o novo personagem ao dicionário 'personagens'.
    personagens[nome] = {
        "forca": int(forca), # Garante que a força seja um inteiro.
        "elemento": elemento
    }
    salvar_personagens() # Salva os personagens atualizados no arquivo.
    print(f"Personagem '{nome}' cadastrado com força {forca} e elemento '{elemento}'.")

def excluir_personagem(nome):
    """
    Exclui um personagem existente do sistema pelo seu nome.

    Args:
        nome (str): O nome do personagem a ser excluído.
    """
    if nome in personagens: # Verifica se o personagem existe.
        del personagens[nome] # Remove o personagem do dicionário.
        salvar_personagens() # Salva as alterações no arquivo.
        print(f"Personagem '{nome}' excluído.")
    else:
        print("Personagem não encontrado.") # Mensagem se o personagem não for encontrado.

def listar_personagens():
    """
    Lista todos os personagens cadastrados no sistema, exibindo seus nomes, força e elemento.
    Retorna uma lista de dicionários de personagens.

    Returns:
        list: Uma lista de dicionários, cada um representando um personagem.
    """
    if not personagens: # Verifica se o dicionário de personagens está vazio.
        print("Nenhum personagem cadastrado.")
        return [] # Retorna uma lista vazia se não houver personagens.

    print("\n=== LISTA DE PERSONAGENS ===")
    lista = [] # Lista para armazenar os dados dos personagens para retorno.
    # Itera sobre cada item (nome e dados) no dicionário 'personagens'.
    for nome, dados in personagens.items():
        print(f"- {nome} (Força: {dados['forca']}, Elemento: {dados['elemento']})")
        # Adiciona os dados do personagem à lista para retorno.
        lista.append({
            "nome": nome,
            "forca": dados["forca"],
            "elemento": dados["elemento"]
        })
    return lista # Retorna a lista de personagens.

def obter_personagem(nome):
    """
    Retorna os dados de um personagem específico pelo nome.

    Args:
        nome (str): O nome do personagem a ser buscado.

    Returns:
        dict or None: Um dicionário com os dados do personagem se encontrado,
                      ou None se o personagem não existir.
    """
    dados = personagens.get(nome) # Tenta obter os dados do personagem pelo nome.
    if dados: # Se os dados forem encontrados.
        return { # Retorna um novo dicionário com os dados do personagem.
            "nome": nome,
            "forca": int(dados["forca"]), # Garante que a força é um inteiro.
            "elemento": dados["elemento"]
        }
    return None # Retorna None se o personagem não for encontrado.

def editar_personagem():
    """
    Permite ao usuário editar o nome, força e/ou elemento de um personagem existente.
    """
    if not personagens: # Verifica se há personagens para editar.
        print("Nenhum personagem cadastrado.")
        return

    print("\n=== EDITOR DE PERSONAGEM ===")
    listar_personagens() # Lista os personagens para o usuário escolher qual editar.

    nome_atual = input("Digite o nome do personagem que deseja editar: ").strip()
    if nome_atual not in personagens: # Verifica se o personagem existe.
        print(f"Personagem '{nome_atual}' não encontrado.")
        return

    personagem = personagens[nome_atual] # Obtém os dados do personagem a ser editado.

    # Edição do nome:
    # Solicita um novo nome, usando o nome atual como padrão se nada for digitado.
    novo_nome = input(f"Novo nome ({nome_atual}): ").strip()
    if not novo_nome:
        novo_nome = nome_atual # Mantém o nome atual se a entrada for vazia.
    elif novo_nome != nome_atual and novo_nome in personagens: # Se o novo nome for diferente e já existir.
        print("Já existe um personagem com esse nome.")
        return

    # Edição da força:
    # Solicita uma nova força, usando a força atual como padrão se nada for digitado.
    try:
        nova_forca = input(f"Nova força ({personagem['forca']}): ").strip()
        nova_forca = int(nova_forca) if nova_forca else personagem['forca']
    except ValueError: # Captura erro se a entrada para força não for um número.
        print("Valor inválido para força.")
        return

    # Edição do elemento:
    print("Escolha o novo elemento:")
    # Lista e ordena os elementos válidos para exibição.
    elementos_ordenados = sorted(list(ELEMENTOS_VALIDOS))
    for i, el in enumerate(elementos_ordenados, 1):
        print(f"{i}. {el.capitalize()}")

    try:
        # Solicita a escolha do novo elemento (número ou ENTER para manter o atual).
        escolha = input(
            f"Elemento atual: {personagem['elemento']} → Nova escolha (1-{len(elementos_ordenados)} ou ENTER para manter): "
        ).strip()

        if escolha: # Se o usuário digitou algo.
            escolha_idx = int(escolha) - 1 # Converte para índice da lista.
            if 0 <= escolha_idx < len(elementos_ordenados): # Verifica se o índice é válido.
                novo_elemento = elementos_ordenados[escolha_idx]
            else:
                print("Escolha inválida.")
                return
        else: # Se o usuário pressionou ENTER (entrada vazia).
            novo_elemento = personagem["elemento"] # Mantém o elemento atual.
    except ValueError: # Captura erro se a entrada para elemento não for um número válido.
        print("Entrada inválida.")
        return

    # Atualiza os dados do personagem no dicionário:
    # Se o nome foi alterado, remove a entrada antiga e adiciona uma nova.
    if nome_atual != novo_nome:
        del personagens[nome_atual]
    personagens[novo_nome] = { # Atualiza ou adiciona o personagem com os novos dados.
        "forca": nova_forca,
        "elemento": novo_elemento
    }

    salvar_personagens() # Salva as alterações no arquivo.
    print(f"Personagem '{nome_atual}' atualizado com sucesso.")