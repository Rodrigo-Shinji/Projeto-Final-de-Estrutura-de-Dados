from batalha import batalhar
from cenarios import escolher_cenario
from historico import exibir_historico
from personagem import (
    cadastrar_personagem, excluir_personagem, carregar_personagens,
    obter_personagem, listar_personagens, editar_personagem, ELEMENTOS_VALIDOS,
)
from times import (
    criar_time, excluir_time, carregar_times, listar_times,
    listar_personagens_do_time, adicionar_personagem_ao_time, remover_personagem_do_time,
    mostrar_personagens_disponiveis, listar_nomes_dos_times
)
from utils import menu_principal, menu_personagens, menu_times, entrada_nome, entrada_inteiro

def selecionar_elemento():
    print("Escolha um elemento:")
    elementos_ordenados_para_selecao = sorted(list(ELEMENTOS_VALIDOS))

    for i, el in enumerate(elementos_ordenados_para_selecao, 1):
        print(f"{i}. {el.capitalize()}")

    while True:
        try:
            opcao = int(input("Digite o número do elemento: "))
            if 1 <= opcao <= len(elementos_ordenados_para_selecao):
                return elementos_ordenados_para_selecao[opcao - 1]
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Digite um número válido.")

def gerenciar_personagens():
    while True:
        opcao = menu_personagens()
        if opcao == '1':
            nome = entrada_nome("Nome do personagem: ")
            forca = entrada_inteiro("Nível de força: ")
            elemento = selecionar_elemento()
            cadastrar_personagem(nome, forca, elemento)
        elif opcao == '2':
            listar_personagens()
            nome = entrada_nome("Nome do personagem a excluir: ")
            excluir_personagem(nome)
        elif opcao == '3':
            listar_personagens()
        elif opcao == '4':
            editar_personagem()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def gerenciar_times():
    while True:
        opcao = menu_times()
        if opcao == '1':
            nome = entrada_nome("Nome do time: ")
            criar_time(nome)
        elif opcao == '2':
            listar_times()
            nome = entrada_nome("Nome do time a excluir: ")
            excluir_time(nome)
        elif opcao == '3':
            listar_times()
        elif opcao == '4':
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            mostrar_personagens_disponiveis()
            nome_pers = entrada_nome("Digite o nome do personagem para adicionar: ")
            adicionar_personagem_ao_time(nome_time, nome_pers)
        elif opcao == '5':
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time)
            nome_pers = entrada_nome("Nome do personagem a remover: ")
            remover_personagem_do_time(nome_time, nome_pers)
        elif opcao == '6':
            listar_times()
            nome_time = entrada_nome("Nome do time: ")
            listar_personagens_do_time(nome_time)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def iniciar_batalha():
    print("\n=== CONFRONTO PvP ===")

    carregar_times()
    times_cadastrados = listar_nomes_dos_times()

    if not times_cadastrados:
        print("Nenhum time cadastrado para iniciar a batalha.")
        return

    while True:
        listar_times()
        time1 = entrada_nome("Nome do primeiro time: ")
        if time1 not in times_cadastrados:
            print(f"Erro: Time '{time1}' não existe. Escolha um time da lista exibida.")
            continue
        break

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
    batalhar(time1, time2, cenario)

def main():
    print("SISTEMA DE TORNEIO DE PERSONAGENS")

    carregar_personagens()
    carregar_times()

    while True:
        opcao = menu_principal()
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

if __name__ == "__main__":
    main()