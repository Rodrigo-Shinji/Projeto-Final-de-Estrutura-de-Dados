# Importa funções específicas do módulo 'personagem' para gerenciar personagens.
from personagem import (
    cadastrar_personagem,  # Adiciona um novo personagem.
    excluir_personagem,    # Remove um personagem existente.
    carregar_personagens,  # Carrega personagens do arquivo.
    obter_personagem,      # Busca os dados de um personagem pelo nome.
    listar_personagens,    # Exibe e retorna uma lista de todos os personagens.
    editar_personagem,     # Permite modificar os dados de um personagem.
    ELEMENTOS_VALIDOS,     # Conjunto de elementos permitidos para personagens.
)

# Importa funções específicas do módulo 'times' para gerenciar times de personagens.
from times import (
    criar_time,                  # Cria um novo time.
    excluir_time,                # Remove um time existente.
    carregar_times,              # Carrega times do arquivo.
    listar_times,                # Exibe e retorna uma lista de todos os times.
    listar_personagens_do_time,  # Lista os personagens de um time específico.
    adicionar_personagem_ao_time,# Adiciona um personagem a um time.
    remover_personagem_do_time,  # Remove um personagem de um time.
    mostrar_personagens_disponiveis, # Exibe personagens que não estão em times.
    listar_nomes_dos_times       # Obtém apenas os nomes dos times cadastrados.
)

# Importa a função principal de batalha do módulo 'batalha'.
from batalha import batalhar

# Importa a função para o usuário escolher o cenário da batalha.
from cenarios import escolher_cenario

# Importa funções auxiliares do módulo 'utils' para menus e entrada de dados.
from utils import menu_principal, menu_personagens, menu_times, entrada_nome, entrada_inteiro

# Importa a função para exibir o histórico de batalhas.
from historico import exibir_historico

def selecionar_elemento():
    """
    Apresenta uma lista de elementos válidos para o usuário escolher.
    Retorna o nome do elemento selecionado (em minúsculas).
    """
    print("Escolha um elemento:")
    # Converte o conjunto de elementos válidos para uma lista e a ordena alfabeticamente
    # para garantir uma exibição consistente e amigável ao usuário.
    elementos_ordenados_para_selecao = sorted(list(ELEMENTOS_VALIDOS))

    # Itera sobre a lista ordenada e exibe cada elemento com um número.
    for i, el in enumerate(elementos_ordenados_para_selecao, 1):
        print(f"{i}. {el.capitalize()}") # Capitaliza a primeira letra do elemento para exibição.

    while True: # Loop para garantir que uma opção válida seja escolhida.
        try:
            opcao = int(input("Digite o número do elemento: ")) # Solicita a escolha do usuário.
            # Verifica se a opção está dentro do intervalo válido.
            if 1 <= opcao <= len(elementos_ordenados_para_selecao):
                # Retorna o elemento correspondente à opção selecionada (subtrai 1 para ajustar ao índice da lista).
                return elementos_ordenados_para_selecao[opcao - 1]
            else:
                print("Escolha inválida.") # Mensagem de erro para opção fora do intervalo.
        except ValueError:
            print("Digite um número válido.") # Mensagem de erro para entrada não numérica.

def gerenciar_personagens():
    """
    Gerencia as operações relacionadas a personagens, como cadastrar, excluir,
    listar e editar. Apresenta um menu de opções ao usuário.
    """
    while True: # Loop principal do menu de gerenciamento de personagens.
        opcao = menu_personagens() # Exibe o menu de personagens e obtém a opção do usuário.
        if opcao == '1': # Opção para cadastrar novo personagem.
            nome = entrada_nome("Nome do personagem: ")
            forca = entrada_inteiro("Nível de força: ")
            elemento = selecionar_elemento() # Solicita ao usuário que selecione um elemento.
            cadastrar_personagem(nome, forca, elemento) # Chama a função de cadastro.
        elif opcao == '2': # Opção para excluir personagem.
            listar_personagens() # Lista os personagens existentes para facilitar a escolha.
            nome = entrada_nome("Nome do personagem a excluir: ")
            excluir_personagem(nome) # Chama a função de exclusão.
        elif opcao == '3': # Opção para listar personagens.
            listar_personagens() # Chama a função para listar todos os personagens.
        elif opcao == '4': # Opção para editar personagem.
            editar_personagem() # Chama a função de edição.
        elif opcao == '0': # Opção para sair do menu de personagens.
            break # Sai do loop e retorna ao menu principal.
        else:
            print("Opção inválida.") # Mensagem para opções não reconhecidas.

def gerenciar_times():
    """
    Gerencia as operações relacionadas a times, como criar, excluir, listar,
    adicionar/remover personagens de times e listar personagens de um time.
    Apresenta um menu de opções ao usuário.
    """
    while True: # Loop principal do menu de gerenciamento de times.
        opcao = menu_times() # Exibe o menu de times e obtém a opção do usuário.
        if opcao == '1': # Opção para criar um novo time.
            nome = entrada_nome("Nome do time: ")
            criar_time(nome) # Chama a função de criação de time.
        elif opcao == '2': # Opção para excluir um time.
            listar_times() # Lista os times existentes.
            nome = entrada_nome("Nome do time a excluir: ")
            excluir_time(nome) # Chama a função de exclusão de time.
        elif opcao == '3': # Opção para listar todos os times.
            listar_times() # Chama a função para listar times.
        elif opcao == '4': # Opção para adicionar personagem a um time.
            listar_times() # Lista os times disponíveis.
            nome_time = entrada_nome("Nome do time: ")
            mostrar_personagens_disponiveis() # Exibe personagens não associados a times.
            nome_pers = entrada_nome("Digite o nome do personagem para adicionar: ")
            adicionar_personagem_ao_time(nome_time, nome_pers) # Chama a função de adição.
        elif opcao == '5': # Opção para remover personagem de um time.
            listar_times() # Lista os times disponíveis.
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time) # Lista os personagens do time para ajudar na escolha.
            nome_pers = entrada_nome("Nome do personagem a remover: ")
            remover_personagem_do_time(nome_time, nome_pers) # Chama a função de remoção.
        elif opcao == '6': # Opção para listar personagens de um time específico.
            listar_times() # Lista os times disponíveis.
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time) # Chama a função para listar personagens de um time.
        elif opcao == '0': # Opção para sair do menu de times.
            break # Sai do loop e retorna ao menu principal.
        else:
            print("Opção inválida.") # Mensagem para opções não reconhecidas.

def iniciar_batalha():
    """
    Coordena o processo de iniciar uma batalha entre dois times.
    Permite ao usuário selecionar os times e o cenário, e então executa a simulação da batalha.
    """
    print("\n=== CONFRONTO PvP ===")

    carregar_times() # Garante que os dados dos times estão atualizados.
    times_cadastrados = listar_nomes_dos_times() # Obtém apenas os nomes dos times.

    if not times_cadastrados: # Verifica se há times cadastrados para batalhar.
        print("Nenhum time cadastrado para iniciar a batalha.")
        return

    # Loop para seleção do primeiro time, garantindo que seja um time existente.
    while True:
        listar_times() # Exibe a lista de times para o usuário.
        time1 = entrada_nome("Nome do primeiro time: ")
        if time1 not in times_cadastrados:
            print(f"Erro: Time '{time1}' não existe. Escolha um time da lista exibida.")
            continue # Continua o loop para que o usuário escolha novamente.
        break # Sai do loop se o time for válido.

    # Loop para seleção do segundo time, garantindo que seja um time existente e diferente do primeiro.
    while True:
        listar_times() # Exibe a lista de times novamente.
        time2 = entrada_nome("Nome do segundo time: ")
        if time2 not in times_cadastrados:
            print(f"Erro: Time '{time2}' não existe. Escolha um time da lista exibida.")
            continue
        if time1 == time2: # Impede que um time batalhe contra si mesmo.
            print("Um time não pode batalhar contra si mesmo.")
            continue
        break
    
    cenario = escolher_cenario() # Permite ao usuário escolher o cenário da batalha.
    batalhar(time1, time2, cenario) # Chama a função principal de batalha.

def main():
    """
    Função principal que inicia o sistema de torneio de personagens.
    Carrega os dados iniciais e apresenta o menu principal ao usuário,
    direcionando para as diferentes funcionalidades do programa.
    """
    print("SISTEMA DE TORNEIO DE PERSONAGENS")

    # Carrega todos os dados persistentes (personagens e times) ao iniciar o programa.
    carregar_personagens()
    carregar_times()

    while True: # Loop principal do sistema, exibindo o menu e processando a opção.
        opcao = menu_principal() # Exibe o menu principal e obtém a opção do usuário.
        if opcao == '1': # Gerenciar personagens.
            gerenciar_personagens()
        elif opcao == '2': # Gerenciar times.
            gerenciar_times()
        elif opcao == '3': # Iniciar uma batalha.
            iniciar_batalha()
        elif opcao == '4': # Exibir histórico de batalhas.
            exibir_historico()
        elif opcao == '0': # Sair do programa.
            print("Encerrando o sistema. Até a próxima!")
            break # Sai do loop e encerra o programa.
        else:
            print("Opção inválida.") # Mensagem para opções não reconhecidas.

# Garante que a função 'main()' só será executada quando o script for rodado diretamente (não quando importado).
if __name__ == "__main__":
    main()