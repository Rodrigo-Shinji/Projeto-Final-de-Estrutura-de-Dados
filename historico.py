import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho completo para o arquivo de histórico dentro da pasta 'data'
ARQUIVO_HISTORICO = os.path.join(BASE_DIR, 'data', 'historico_batalhas.json')

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        if os.path.getsize(ARQUIVO_HISTORICO) > 0:
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return []
    return []


def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

def registrar_batalha(time1, time2, vencedor):
    historico = carregar_historico()
    registro = {
        'time1': time1,
        'time2': time2,
        'vencedor': vencedor,
        
    }
    historico.append(registro)
    salvar_historico(historico)

def exibir_historico():
    historico = carregar_historico()
    if not historico:
        print("Nenhuma batalha registrada.")
        return
    print("\n=== HISTÓRICO DE BATALHAS ===")
    for idx, batalha in enumerate(historico, 1):
        print(f"{idx}. {batalha['time1']} vs {batalha['time2']} - Vencedor: {batalha['vencedor']}")

