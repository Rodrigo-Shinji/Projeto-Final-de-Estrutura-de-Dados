def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Gerenciar Personagens")
    print("2. Gerenciar Times")
    print("3. Iniciar Batalha (PvP)")
    print("4. Ver Histórico de Batalhas")
    print("0. Sair")
    return input("Escolha uma opção: ")


def menu_personagens():
    print("\n=== MENU DE PERSONAGENS ===")
    print("1. Cadastrar Personagem")
    print("2. Excluir Personagem")
    print("3. Listar Personagens")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_times():
    print("\n=== MENU DE TIMES ===")
    print("1. Criar Time")
    print("2. Excluir Time")
    print("3. Listar Times")
    print("4. Inserir Personagem no Time")
    print("5. Remover Personagem do Time")
    print("6. Listar Personagens de um Time")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def entrada_inteiro(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("⚠️ Valor inválido. Digite um número inteiro.")

def entrada_nome(msg):
    nome = input(msg).strip()
    while not nome:
        print("⚠️ Nome não pode ser vazio.")
        nome = input(msg).strip()
    return nome