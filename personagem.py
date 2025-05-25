import json
import os

personagens = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "data", "personagens.json")

ELEMENTOS_VALIDOS = {"fogo", "terra", "luz", "trevas", "agua", "vento"}

def carregar_personagens():
    global personagens
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                personagens = json.load(f)
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON do arquivo de personagens em: {ARQUIVO}. Iniciando com personagens vazios.")
            personagens = {}
    else:
        personagens = {}

def salvar_personagens():
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=4, ensure_ascii=False)

def cadastrar_personagem(nome, forca, elemento):
    if nome in personagens:
        print("Personagem já existe.")
        return
    if elemento not in ELEMENTOS_VALIDOS:
        print(f"Elemento inválido. Escolha entre: {', '.join(sorted(list(ELEMENTOS_VALIDOS)))}")
        return

    personagens[nome] = {
        "forca": int(forca),
        "elemento": elemento
    }
    salvar_personagens()
    print(f"Personagem '{nome}' cadastrado com força {forca} e elemento '{elemento}'.")

def excluir_personagem(nome):
    if nome in personagens:
        del personagens[nome]
        salvar_personagens()
        print(f"Personagem '{nome}' excluído.")
    else:
        print("Personagem não encontrado.")

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

def obter_personagem(nome):
    dados = personagens.get(nome)
    if dados:
        return {
            "nome": nome,
            "forca": int(dados["forca"]),
            "elemento": dados["elemento"]
        }
    return None

def editar_personagem():
    if not personagens:
        print("Nenhum personagem cadastrado.")
        return

    print("\n=== EDITOR DE PERSONAGEM ===")
    listar_personagens()

    nome_atual = input("Digite o nome do personagem que deseja editar: ").strip()
    if nome_atual not in personagens:
        print(f"Personagem '{nome_atual}' não encontrado.")
        return

    personagem = personagens[nome_atual]

    novo_nome = input(f"Novo nome ({nome_atual}): ").strip()
    if not novo_nome:
        novo_nome = nome_atual
    elif novo_nome != nome_atual and novo_nome in personagens:
        print("Já existe um personagem com esse nome.")
        return

    try:
        nova_forca = input(f"Nova força ({personagem['forca']}): ").strip()
        nova_forca = int(nova_forca) if nova_forca else personagem['forca']
    except ValueError:
        print("Valor inválido para força.")
        return

    print("Escolha o novo elemento:")
    elementos_ordenados = sorted(list(ELEMENTOS_VALIDOS))
    for i, el in enumerate(elementos_ordenados, 1):
        print(f"{i}. {el.capitalize()}")

    try:
        escolha = input(
            f"Elemento atual: {personagem['elemento']} → Nova escolha (1-{len(elementos_ordenados)} ou ENTER para manter): "
        ).strip()

        if escolha:
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(elementos_ordenados):
                novo_elemento = elementos_ordenados[escolha_idx]
            else:
                print("Escolha inválida.")
                return
        else:
            novo_elemento = personagem["elemento"]
    except ValueError:
        print("Entrada inválida.")
        return

    del personagens[nome_atual]
    personagens[novo_nome] = {
        "forca": nova_forca,
        "elemento": novo_elemento
    }

    salvar_personagens()
    print(f"Personagem '{nome_atual}' atualizado com sucesso.")