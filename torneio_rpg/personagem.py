import json
import os

# Dicionário para armazenar personagens em memória enquanto o programa roda
personagens = {}

# Obtém o diretório base onde o script está sendo executado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho completo para o arquivo JSON que guarda os personagens, dentro da pasta "data"
ARQUIVO = os.path.join(BASE_DIR, "data", "personagens.json")


# Função para carregar os personagens do arquivo JSON para o dicionário em memória
def carregar_personagens():
    global personagens  # Indica que a função vai modificar a variável global 'personagens'
    if os.path.exists(ARQUIVO):  # Verifica se o arquivo existe
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            personagens = json.load(f)  # Lê o conteúdo JSON e carrega no dicionário 'personagens'
    else:
        personagens = {}  # Se o arquivo não existir, inicia o dicionário vazio


# Função para salvar o dicionário de personagens no arquivo JSON
def salvar_personagens():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(personagens, f, indent=4, ensure_ascii=False)  # Serializa o dicionário em JSON no arquivo


# Função para cadastrar um novo personagem
def cadastrar_personagem(nome, forca):
    if nome in personagens:  # Verifica se personagem já existe
        print("Personagem já existe.")
        return
    personagens[nome] = {"forca": int(forca)}  # Adiciona personagem com força convertida para inteiro
    salvar_personagens()  # Salva alterações no arquivo
    print(f"Personagem '{nome}' cadastrado com força {forca}.")


# Função para excluir um personagem pelo nome
def excluir_personagem(nome):
    if nome in personagens:
        del personagens[nome]  # Remove personagem do dicionário
        salvar_personagens()  # Atualiza o arquivo
        print(f"Personagem '{nome}' excluído.")
    else:
        print("Personagem não encontrado.")


# Função para listar todos os personagens cadastrados
def listar_personagens():
    if not personagens:
        print("Nenhum personagem cadastrado.")
        return
    print("\n=== LISTA DE PERSONAGENS ===")
    for nome, dados in personagens.items():
        print(f"- {nome} (Força: {dados['forca']})")  # Exibe nome e força de cada personagem


# Função para obter os dados de um personagem específico pelo nome
def obter_personagem(nome):
    dados = personagens.get(nome)  # Busca personagem no dicionário
    if dados:
        return {"nome": nome, "forca": int(dados["forca"])}  # Retorna dicionário com nome e força
    return None  # Retorna None se personagem não encontrado
