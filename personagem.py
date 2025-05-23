import json
import os

# Dicionário para armazenar personagens em memória durante a execução do programa
personagens = {}

# Define o diretório base onde o script está sendo executado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo JSON onde os personagens serão salvos e carregados
ARQUIVO = os.path.join(BASE_DIR, "data", "personagens.json")

# Lista fixa com os elementos disponíveis que um personagem pode ter
ELEMENTOS_VALIDOS = ["fogo", "terra", "luz", "trevas", "agua", "vento"]

# Função para carregar os personagens do arquivo JSON para a memória
def carregar_personagens():
    global personagens
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            personagens = json.load(f)
    else:
        personagens = {}

# Função para salvar os personagens da memória no arquivo JSON
def salvar_personagens():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=4, ensure_ascii=False)

# Função para cadastrar um novo personagem no sistema
def cadastrar_personagem(nome, forca, elemento):
    if nome in personagens:
        print("⚠️ Personagem já existe.")
        return
    if elemento not in ELEMENTOS_VALIDOS:
        print(f"❌ Elemento inválido. Escolha entre: {', '.join(ELEMENTOS_VALIDOS)}")
        return

    # Adiciona o personagem ao dicionário
    personagens[nome] = {
        "forca": int(forca),
        "elemento": elemento
    }
    salvar_personagens()
    print(f"✅ Personagem '{nome}' cadastrado com força {forca} e elemento '{elemento}'.")

# Função para excluir um personagem do sistema
def excluir_personagem(nome):
    if nome in personagens:
        del personagens[nome]
        salvar_personagens()
        print(f"Personagem '{nome}' excluído.")
    else:
        print("Personagem não encontrado.")

# Função que lista todos os personagens cadastrados no sistema
def listar_personagens():
    if not personagens:
        print("Nenhum personagem cadastrado.")
        return []

    print("\n=== LISTA DE PERSONAGENS ===")
    lista = []
    for nome, dados in personagens.items():
        print(f"- {nome} (Força: {dados['forca']}, Elemento: {dados['elemento']})")
        lista.append({
            "nome": nome,
            "forca": dados["forca"],
            "elemento": dados["elemento"]
        })
    return lista

# Função que retorna os dados de um personagem específico pelo nome
def obter_personagem(nome):
    dados = personagens.get(nome)
    if dados:
        return {
            "nome": nome,
            "forca": int(dados["forca"]),
            "elemento": dados["elemento"]
        }
    return None

# Função que permite editar os dados de um personagem existente
def editar_personagem():
    if not personagens:
        print("⚠️ Nenhum personagem cadastrado.")
        return

    print("\n=== EDITOR DE PERSONAGEM ===")
    listar_personagens()

    # Escolhe o personagem a editar
    nome_atual = input("Digite o nome do personagem que deseja editar: ").strip()
    if nome_atual not in personagens:
        print(f"❌ Personagem '{nome_atual}' não encontrado.")
        return

    personagem = personagens[nome_atual]

    # Entrada para novo nome
    novo_nome = input(f"Novo nome ({nome_atual}): ").strip()
    if not novo_nome:
        novo_nome = nome_atual
    elif novo_nome != nome_atual and novo_nome in personagens:
        print("⚠️ Já existe um personagem com esse nome.")
        return

    # Entrada para nova força
    try:
        nova_forca = input(f"Nova força ({personagem['forca']}): ").strip()
        nova_forca = int(nova_forca) if nova_forca else personagem['forca']
    except ValueError:
        print("⚠️ Valor inválido para força.")
        return

    # Escolher novo elemento
    print("🌟 Escolha o novo elemento:")
    for i, el in enumerate(ELEMENTOS_VALIDOS, 1):
        print(f"{i}. {el.capitalize()}")

    try:
        escolha = input(
            f"Elemento atual: {personagem['elemento']} → Nova escolha (1-{len(ELEMENTOS_VALIDOS)} ou ENTER para manter): "
        ).strip()

        if escolha:
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(ELEMENTOS_VALIDOS):
                novo_elemento = ELEMENTOS_VALIDOS[escolha_idx]
            else:
                print("⚠️ Escolha inválida.")
                return
        else:
            novo_elemento = personagem["elemento"]
    except ValueError:
        print("⚠️ Entrada inválida.")
        return

    # Atualiza os dados do personagem no dicionário
    del personagens[nome_atual]  # remove o antigo
    personagens[novo_nome] = {
        "forca": nova_forca,
        "elemento": novo_elemento
    }

    salvar_personagens()
    print(f"✅ Personagem '{nome_atual}' atualizado com sucesso.")