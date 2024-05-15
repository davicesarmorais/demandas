from lib.lib import *
from lib.cores import *
from datetime import datetime
from time import sleep


def outra_data(numero_demanda, quantidade_horas):
    while True:
        print("Digite a data (ou 'q' para voltar)")
        entrada_data = input("> ")
        
        if entrada_data == "q" or not entrada_data:
            return "voltar"
        
        if (data := formatar_data(entrada_data=entrada_data)) == "formato invalido":
            continue
        
        alterar_data(data, numero_demanda, quantidade_horas)
        break


def alterar_data(data, numero_demanda, quantidade_horas):
    if data in demandas[numero_demanda]["datas"]:
        demandas[numero_demanda]["datas"][data] += int(quantidade_horas)
    else:
        demandas[numero_demanda]["datas"].update({data: int(quantidade_horas)})
        
    salvar_no_json()
    print(f"{verde}Quantidade de horas atualizado com sucesso!{reset}")
    sleep(0.5)


def pesquisar_demanda(numero_demanda):
    while True:
        limpar_terminal()
        printar_uma_demanda(numero_demanda, com_horas=True)
        print("Digite a quantidade de horas que quer adicionar (ou 'q' para sair)")

        while True:
            quantidade_horas = input("> ")
            
            if quantidade_horas == "q" or not quantidade_horas:
                return
                  
            if not quantidade_horas.isdecimal():
                print(f"{red}Digite um número inteiro{reset}")
                continue
            break
        
        
        while True:
            limpar_terminal()
            printar_uma_demanda(numero_demanda, com_horas=True)
            print("1. Data atual\n2. Outra data\n3. Voltar (enter)")
            entrada = input("> ")
            
            match entrada:
                case "" | "q" | "3":
                    break
                
                case "1":
                    data = datetime.now().strftime("%d/%m/%Y")
                    alterar_data(data, numero_demanda, quantidade_horas)
                    break
                
                case "2":
                    if outra_data(numero_demanda, quantidade_horas) == "voltar":
                        continue
                    else:
                        break
                