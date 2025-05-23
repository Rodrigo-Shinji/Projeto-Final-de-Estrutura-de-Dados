# Importa funções do módulo 'personagem' relacionadas ao gerenciamento de personagens
from personagem import (
    cadastrar_personagem, excluir_personagem, carregar_personagens,
    obter_personagem, listar_personagens, editar_personagem , ELEMENTOS_VALIDOS,
)

# Importa funções do módulo 'times' relacionadas ao gerenciamento de times
from times import (
    criar_time, excluir_time, carregar_times, listar_times,
    listar_personagens_do_time, adicionar_personagem_ao_time, remover_personagem_do_time,
)

# Importa a função que executa a lógica da batalha entre dois times
from batalha import batalhar

from cenarios import escolher_cenario

# Importa funções auxiliares como os menus e entrada de dados
from utils import menu_principal, menu_personagens, menu_times, entrada_nome, entrada_inteiro

from historico import exibir_historico

def selecionar_elemento():
    print("🌟 Escolha um elemento:")
    for i, el in enumerate(ELEMENTOS_VALIDOS, 1):
        print(f"{i}. {el.capitalize()}")
    while True:
        try:
            opcao = int(input("Digite o número do elemento: "))
            if 1 <= opcao <= len(ELEMENTOS_VALIDOS):
                return ELEMENTOS_VALIDOS[opcao - 1]
            else:
                print("⚠️ Escolha inválida.")
        except ValueError:
            print("⚠️ Digite um número válido.")

# Função que gerencia as ações disponíveis no menu de personagens
def gerenciar_personagens():
    while True:
        opcao = menu_personagens()  # Exibe o menu e lê a opção escolhida
        if opcao == '1':  # Cadastro de novo personagem
            nome = entrada_nome("Nome do personagem: ")
            forca = entrada_inteiro("Nível de força: ")
            elemento = selecionar_elemento()
            cadastrar_personagem(nome, forca, elemento)  # Chama a função de cadastro
        elif opcao == '2':  # Exclusão de personagem existente
            listar_personagens()  # Lista antes de permitir a exclusão
            nome = entrada_nome("Nome do personagem a excluir: ")
            excluir_personagem(nome)
        elif opcao == '3':  # Lista todos os personagens cadastrados
            listar_personagens()
        elif opcao == '4':
            editar_personagem()
        elif opcao == '0':  # Sai do menu de personagens
            break
        else:
            print("Opção inválida.")  # Caso a opção digitada não seja válida


# Função que gerencia as ações disponíveis no menu de times
def gerenciar_times():
    while True:
        opcao = menu_times()  # Exibe o menu e lê a opção escolhida
        if opcao == '1':  # Criação de um novo time
            nome = entrada_nome("Nome do time: ")
            criar_time(nome)
        elif opcao == '2':  # Exclusão de um time
            listar_times()
            nome = entrada_nome("Nome do time a excluir: ")
            excluir_time(nome)
        elif opcao == '3':  # Listagem de todos os times
            listar_times()
        elif opcao == '4':  # Adição de personagem a um time
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            from times import mostrar_personagens_disponiveis
            mostrar_personagens_disponiveis()  # exibe só uma vez
            nome_pers = entrada_nome("Digite o nome do personagem para adicionar: ")
            adicionar_personagem_ao_time(nome_time, nome_pers)
        elif opcao == '5':  # Remoção de personagem de um time
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time)  # já imprime tudo internamente
            nome_pers = entrada_nome("Nome do personagem a remover: ")
            remover_personagem_do_time(nome_time, nome_pers)
        elif opcao == '6':  # Listagem dos personagens de um time específico
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time)
        elif opcao == '0':  # Sai do menu de times
            break
        else:
            print("Opção inválida.")  # Caso a opção digitada não seja válida


# Função que realiza o fluxo de batalha entre dois times
def iniciar_batalha():
    print("\n=== CONFRONTO PvP ===")

    # Garante que os dados dos times estão atualizados ao recarregar do arquivo
    carregar_times()
    from times import listar_nomes_dos_times  # Importa função para obter apenas os nomes
    times_cadastrados = listar_nomes_dos_times()

    if not times_cadastrados:  # Nenhum time criado ainda
        print("Nenhum time cadastrado para iniciar a batalha.")
        return

    # Loop para seleção do primeiro time (verifica se é válido)
    while True:
        listar_times()
        time1 = entrada_nome("Nome do primeiro time: ")
        if time1 not in times_cadastrados:
            print(f"Erro: Time '{time1}' não existe. Escolha um time da lista exibida.")
            continue
        break

    # Loop para seleção do segundo time (diferente do primeiro e válido)
    while True:
        listar_times()
        time2 = entrada_nome("Nome do segundo time: ")
        if time2 not in times_cadastrados:
            print(f"Erro: Time '{time2}' não existe. Escolha um time da lista exibida.")
            continue
        if time1 == time2:
            print("Um time não pode batalhar contra si mesmo.")
            continue
        break
    
    cenario = escolher_cenario()
    # Inicia a batalha entre os dois times selecionados
    batalhar(time1, time2, cenario)


# Função principal que gerencia o sistema como um todo
def main():
    print("SISTEMA DE TORNEIO DE PERSONAGENS")

    # Carrega personagens, times e histórico previamente salvos em arquivos
    carregar_personagens()
    carregar_times()

    while True:
        opcao = menu_principal()  # Mostra o menu principal
        if opcao == '1':
            gerenciar_personagens()
        elif opcao == '2':
            gerenciar_times()
        elif opcao == '3':
            iniciar_batalha()
        elif opcao == '4':
            exibir_historico()
        elif opcao == '0':
            print("Encerrando o sistema. Até a próxima!")
            break
        else:
            print("Opção inválida.")


# Garante que o programa só será executado se este arquivo for o principal
if __name__ == "__main__":
    main()

