from lib.cores import *
from lib.lib import demandas, salvar_no_json, printar_numero_e_titulo, limpar_terminal
from time import sleep
from cadastro.editar_demandas import editar_demandas, get_numero_demanda


def get_estimativa() -> str:
    while True:
        estimativa = input("Digite a estimativa de horas da demanda: ")

        if estimativa == "q" or not estimativa:
            return "sair"

        if not estimativa.isdecimal():
            print(f"{red}Digite um número.{reset}")
            sleep(0.5)
            continue

        return estimativa


def get_titulo() -> str:
    titulo = input("Digite o TÍTULO da demanda: ")

    if titulo == "q" or not titulo:
        return "sair"

    return titulo


def adicionar_demandas() -> None:
    limpar_terminal()
    print(f"{azul}Para cancelar a qualquer momento digite 'q'{reset}\n")

    if (numero_demanda := get_numero_demanda()) == "sair":
        return

    if (titulo := get_titulo()) == "sair":
        return

    if (estimativa := get_estimativa()) == "sair":
        return

    cadastro_dict = {
        numero_demanda: {
            "titulo": titulo,
            "estimativa": int(estimativa),
            "status": "ativa",
            "datas": {},
        }
    }

    demandas.update(cadastro_dict)
    salvar_no_json("demandas.json", demandas)
    print(f"{verde}Demanda ({numero_demanda}) adicionada com sucesso!{reset}")
    sleep(1)


def remover_demandas() -> None:
    limpar_terminal()
    print(f"{'{ Demandas }':-^80}")
    printar_numero_e_titulo()
    print("-" * 80)
    while True:
        numero_demanda = input(
            "Digite o número da demanda que deseja remover (ou 'q' para cancelar): "
        )

        if numero_demanda == "q" or not numero_demanda:
            return

        if numero_demanda not in demandas:
            print(f"{red}Demanda não encontrada.{reset}")
            sleep(0.5)
            continue

        print(
            f"{azul}Você realmente deseja excluir a demanda {numero_demanda}? (s/n){reset}"
        )
        confirmacao = input("> ")

        if confirmacao == "s":
            del demandas[numero_demanda]
            salvar_no_json("demandas.json", demandas)
            print(f"{verde}Demanda {numero_demanda} excluída com sucesso.{reset}")
            sleep(1)
            return

        else:
            print(f"{azul}Operação cancelada.{reset}")
            sleep(0.5)
            continue


def add_remove_edit_demanda() -> None:
    while True:
        limpar_terminal()
        print("1. Adicionar demanda")
        print("2. Remover demanda")
        print("3. Editar demanda")
        print("4. Voltar (enter)")

        entrada = input("> ")
        match entrada:

            case "4" | "":  # Voltar
                break

            case "1": 
                adicionar_demandas()

            case "2":
                remover_demandas()

            case "3":
                editar_demandas()
