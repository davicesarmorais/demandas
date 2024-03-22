import os
import time
import json
from datetime import datetime, timedelta
from colorama import init, Fore
init()
verde = Fore.GREEN
azul = Fore.LIGHTBLUE_EX
amarelo = Fore.YELLOW
red = Fore.LIGHTRED_EX
roxo = Fore.LIGHTMAGENTA_EX

def salvar_horas(data,soma):
    computar_dict = {}
    computar_dict = {data: int(computar_horas) + soma}
    demandas[num]["datas"].update(computar_dict)
    with open("demandas.json" , "w") as f:
        json.dump(demandas , f, indent=4)
    print("Horas computadas com sucesso!")
    time.sleep(1)

def atualizar_demanda(texto, printar):
    with open("demandas.json", "w") as f:
        json.dump(demandas, f, indent=4)
    if printar == True:
        print(texto)
        time.sleep(1)

def printar_demanda():
    status = demandas[num]['status']
    print(amarelo + f"{num} - {demandas[num]['titulo']}" + Fore.RESET)
    print(f"Estimativa: {roxo}{demandas[num]['estimativa']}h{Fore.RESET}")
    print(f"Status: {verde + status + Fore.RESET if status == 'concluida' else azul + status + Fore.RESET}")
    print(f"Horas gastas: {verde}{soma}h{Fore.RESET}")
    print(f"Horas restantes: {red}{diferenca}h{Fore.RESET}")

def calc_data(condicao):
    if condicao:
        data = datetime.now().date().strftime("%d/%m/%Y")
    else:
        data = input("Digite a data (formato: dia/mes/ano): ")
    
    if data in demandas[num]["datas"]:
        salvar_horas(data, demandas[num]["datas"][data])
    else:
        salvar_horas(data, 0)

def settings_data():
    os.system("cls")
    print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
    data_settings = input("> ")
    match data_settings:
        case "1": # data auto (- detalhes)
            calc_data(True)
        case "2":
            calc_data(False)

while True: # loop principal
    demanda_numero = [] # sempre recomeçar vazio para nâo dar erro
    demanda_titulo = []

    try:
        with open("demandas.json", 'r') as f: # abrir json e mandar demanda_numero e demanda_titulo para  lista
            demandas = json.load(f)
            for numero in demandas:
                demanda_numero.append(numero)
                demanda_titulo.append(demandas[numero]["titulo"])
                if 'status' not in demandas[numero]:
                    demandas[numero]['status'] = "ativa"
                    atualizar_demanda(None,False)
                
                
    except FileNotFoundError: # cria arquivo json se nao existir
        demandas = {}
        with open("demandas.json", 'w') as f:
            json.dump(demandas, f, indent=4) 
    
    os.system("cls")
    print(f"{"Demandas":-^100}")
    for numero in demandas:
        num_e_dem = f"{numero} - {demandas[numero]['titulo']}"
        print(f"{num_e_dem: ^100}")
    print("-" * 100)
    print("\n1. Pesquisar demanda",
          "\n2. Cadastrar/Editar demanda",
          "\n3. Ver relatórios de apontamentos",
          "\n4. Listar demandas em execução",
          "\n5. Listar demandas concluídas",
          "\n6. Salvar e fechar programa",
          "\n[?] - Ajuda")
    
    principal_input = (input("> "))
    match principal_input:
        
        case "1":  # Pesquisar demandas
            digitar_num_titulo = input("Digite o número ou o titulo da demanda: ")
            if digitar_num_titulo not in demanda_numero and digitar_num_titulo not in demanda_titulo:
                print("Demanda não encontrada.")
                time.sleep(1)          
            
            else:
                if not digitar_num_titulo.isdigit(): # se nao for um numero (numero da demanda) puxa o valor do titulo por meio de indexagem do numeri
                    num = demanda_numero[demanda_titulo.index(digitar_num_titulo)]
                else:
                    num = digitar_num_titulo
                lista_data = list(demandas[num]["datas"].items()) # datas vao para uma lista par melhor menipulação
                soma = 0
                for item in lista_data:
                    soma = soma + int(item[1]) # soma de horas gastas
                diferenca = int(demandas[num]['estimativa']) - soma  # horas restantes         
                
                while True: 
                    os.system("cls")
                    printar_demanda()              
                    print()
                    for item in lista_data:
                        print(f"{item[0]}: {item[1]}h")
                            
                    print("\n1. Inputar horas\n2. Marcar como concluida/ativa\n3. Voltar (enter)")
                    input_horas_ver_detalhes = input("> ")
                    match input_horas_ver_detalhes:
                    
                        case "1": # 
                            computar_horas = input("Digite as horas: ")
                            if computar_horas == "" or not computar_horas.isdigit():
                                print("Operação cancelada ou formato inválido.")
                                time.sleep(1)
                            else:                   
                                settings_data()
                                break

                        case "2":
                            if demandas[num]["status"] == "ativa":
                                print("Você deseja marcar essa demanda como concluída? (s/n)")
                                decisao = input("> ")
                                if decisao.upper() == "S":
                                    demandas[num]["status"] = "concluida"
                                    atualizar_demanda("Demanda atualizada com sucesso!", True)

                            elif demandas[num]["status"] == "concluida":
                                print("Você deseja marca essa demanda como ativa? (s/n)")
                                decisao = input("> ")
                                if decisao.upper() == "S":
                                    demandas[num]["status"] = "ativa"
                                    atualizar_demanda("Demanda atualizada com sucesso!", True)
                        
                        case "3"|"": # voltar
                            break