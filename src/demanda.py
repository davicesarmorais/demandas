import os
import time
import json
from datetime import datetime
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
    print("1. Pesquisar demanda.\n2. Cadastrar/Editar demanda.\n3. Relatórios\n4. Listar demandas em execução\n5. Listar demandas concluídas.\n6. Salvar e fechar programa.")
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
                    print("\n1. Inputar horas\n2. Marcar como concluida/ativa\n3. Ver detalhes\n4. Voltar (enter)")
                    input_horas_ver_detalhes = input("> ")
                    match input_horas_ver_detalhes:
                    
                        case "1": # Computar horas (- detalhes)
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
                        
                        case "3": # Ver detalhes
                            os.system("cls")
                            printar_demanda() 
                            print()
                            for item in lista_data:
                                print(f"{item[0]}: {item[1]}h")
                            
                            print("\n1. Inputar horas\n2. Ver menos detalhes\n3. Voltar tudo (enter)")
                            input_horas_ver_detalhes = input("> ")     
                            match input_horas_ver_detalhes:
                                
                                case "1": # Computar horas (+ detalhes)
                                    computar_horas = input("Digite as horas: ")
                                    if computar_horas == "" or not computar_horas.isdigit():
                                        print("Operação cancelada ou formato inválido.")
                                        time.sleep(1)
                                    else:
                                        settings_data()
                                        break                       
                                
                                case "2": # ver menos detalhes
                                    os.system("cls")
                                case "3"|"": # voltar
                                    break
                        case "4"|"": # voltar
                            break
      
        case "2": # Cadastrar demandas principal
            while True:
                os.system("cls")
                print("1. Adicionar demanda\n2. Remover demanda\n3. Editar demanda\n4. Voltar (enter)")
                editar_input = input("> ")
                match editar_input:
                    case "4"|"":
                        break
                    case "1": # Adicionar demanda
                        os.system("cls")
                        print("Para voltar a qualquer momento aperte 'Enter'\n")
                        cadastrar_numero = input("Digite o NÚMERO da demanda: ") # cadastrar numero
                        
                        if cadastrar_numero != "" and cadastrar_numero not in demandas:
                            cadastrar_titulo = input("Digite o TÍTULO da demanda: ") # cadastrar titulo
                            
                            if cadastrar_titulo != "":    # cadastrar estimativa
                                cadastrar_estimativa = input("Digite a estimativa de horas da demanda: ")
                                
                                if str(cadastrar_estimativa) != "" and cadastrar_estimativa.isdigit():    
                                    cadastro_dict = {}
                                    cadastro_dict[cadastrar_numero] = {"titulo": cadastrar_titulo, "estimativa": int(cadastrar_estimativa), "status": "ativa", "datas": {}}
                                    demandas.update(cadastro_dict)
                                    atualizar_demanda(None, False) # atualizar lista
                                    print(f"Demanda ({cadastrar_numero}) adicionada com sucesso!")
                                    time.sleep(2)
                                    break
                                else:
                                    print("Operação cancelada ou formato inválido.")
                                    time.sleep(1.5)
                        else:
                            print("Operação cancelada ou número já registrado.")
                            time.sleep(1.5)
                    
                    case "2": # Remover demanda
                        remover_demanda = input("Digite o número da demanda que deseja remover: ")
                        if remover_demanda != "":
                            if remover_demanda not in demandas:
                                print("Demanda não encontrada.")
                                time.sleep(1.5)
                            else:
                                print(f"Você realmente deseja excluir a demanda {remover_demanda}? (s/n)")
                                confirmacao = input("> ")
                                if confirmacao.upper() == "S":
                                    del demandas[remover_demanda]
                                    atualizar_demanda(None, False)
                                    print(f"Demanda {remover_demanda} excluída com sucesso.")
                                    time.sleep(1)
                    
                    case "3": # Editar demanda
                        editar_demanda = input("Digite o número da demanda que quer editar: ")
                        if editar_demanda not in demandas:
                            print("Demanda não encontrada")
                            time.sleep(1)
                        else:
                            os.system("cls")
                            a = demandas[editar_demanda]
                            lista_data = list(demandas[editar_demanda]["datas"].items())
                            print(amarelo + f"{editar_demanda}: {a['titulo']}" + Fore.RESET)
                            print(f"Estimativa: {roxo}{a['estimativa']}h{Fore.RESET}")
                            for data in lista_data:
                                print(f"{data[0]}: {data[1]}h")
                            print("\nDigite qual a informação que deseja alterar (Ex: 'numero', 'titulo', 'estimativa', 'data', 'hora')")
                            escolher_info = input("> ")
                            match escolher_info:
                            
                                case "titulo": # Editar titulo
                                    editar_titulo = input("Digite o novo nome do titulo: ")
                                    if editar_titulo != "":
                                        print(f"Você deseja confirmar a alteração para '{editar_titulo}'? (s/n)")
                                        choice = input("> ")
                                        if choice.upper() == "S":
                                            demandas[editar_demanda]["titulo"] = editar_titulo
                                            atualizar_demanda("Demanda atualizada com sucesso!", True)
                                            break

                                case "estimativa": # Editar estimativa
                                    editar_estimativa = input("Digite a nova quantidade de horas de estimativa: ")
                                    if editar_estimativa != "":
                                        print(f"Você deseja confirmar a alteração para {editar_estimativa}h? (s/n)")
                                        choice = input("> ")
                                        if choice in ["s", "S"] and editar_estimativa.isdigit():
                                            demandas[editar_demanda]["estimativa"] = int(editar_estimativa)
                                            atualizar_demanda("Demanda atualizada com sucesso!", True)
                                            break
                                        else:
                                            os.system("cls")
                                            print("Operação cancelada.")
                                            time.sleep(1.5)

                                case "data"|"datas"|"horas"|"hora": # Editar data, horas
                                    editar_data = input("Digite a data que quer editar, excluir ou modificar horas: ")
                                    if editar_data == "" or editar_data not in demandas[editar_demanda]["datas"]:
                                        os.system("cls")
                                        print("Operação cancelada")
                                        time.sleep(1.5)
                                    
                                    else:
                                        print("1. Mudar data\n2. Mudar horas\n3. Exluir data\n4. Voltar (enter)")
                                        choice2 = input("> ")
                                        match choice2:
                                            
                                            case "1": # Editar data
                                                trocar_data = input("Digite a nova data. Formato: (dia/mes/anos): ")
                                                if trocar_data == "":
                                                    print("Operação cancelada.")
                                                    time.sleep(1)
                                                else:
                                                    print(f"Você deseja confirmar a alteração para '{trocar_data}'? (s/n)")
                                                    choice = input("> ")
                                                    if choice in ["s", "S"]:
                                                        x = demandas[editar_demanda]["datas"][editar_data]
                                                        del demandas[editar_demanda]["datas"][editar_data]
                                                        demandas[editar_demanda]["datas"][trocar_data] = x
                                                        atualizar_demanda("Demanda atualizada com sucesso!", True)
                                                        break
                                            
                                            case "2": # Editar horas
                                                escolha_horas = input("Digite a nova quantidade de horas: ")
                                                if escolha_horas != "" and escolha_horas.isdigit():
                                                    certeza = input(f"Você tem certeza que quer alterar as horas para {escolha_horas}h? (s/n): ")
                                                    if certeza.upper() == "S":
                                                        demandas[editar_demanda]["datas"][editar_data] = int(escolha_horas)
                                                        atualizar_demanda("Demanda atualizada com sucesso!", True)
                                                        break
                                                else:
                                                    os.system("cls")
                                                    print("Operação cancelada.")
                                                    time.sleep(1.5)
                                            
                                            case "3": # Excluir data
                                                print(f"Você tem certeza que quer excluir a data {editar_data} da demanda {editar_demanda}? (s/n)")
                                                choice3 = input("> ")
                                                if choice3.upper() == "S":
                                                    del demandas[editar_demanda]["datas"][editar_data]
                                                    atualizar_demanda('Data excluída com sucesso!', True)
                                                    break
                           
                                case "numero": # Editar numero demanda
                                    escolha_numero = input("Digite o novo número da demanda: ")
                                    if escolha_numero != ""and escolha_numero not in demandas:
                                        print(f"Você tem certeza que deseja alterar o número dessa demanda para {escolha_numero}? (s/n)")
                                        decisao = input("> ")
                                        if decisao.upper() == "S":
                                            x = demandas[editar_demanda]
                                            del demandas[editar_demanda]
                                            demandas[escolha_numero] = x
                                            atualizar_demanda("Demanda atualizada com sucesso!", True) 
                                    else:
                                        print("Operação cancelada ou número já registrado.")
                                        time.sleep(1)
                                                                
        case "3": # Relatórios
            while True:
                os.system('cls')
                print("1. Data específica.\n2. Mês específico.\n3. Período.\n4. Voltar (enter).")
                relatorio_input = input("> ")
                match relatorio_input:
                    case "1":
                        data_especifica = input("Digite uma data específica (Formato: dd/mm/yyyy): ")
                        if data_especifica != "":
                            os.system('cls')
                            soma = 0
                            for num in demandas:
                                if data_especifica in demandas[num]["datas"]:
                                    soma = soma + demandas[num]["datas"][data_especifica]
                                    print(f"{amarelo + num} - {demandas[num]['titulo'] + Fore.RESET}")
                                    print(azul + f"Horas registradas nessa data: {demandas[num]['datas'][data_especifica]}" + Fore.RESET)
                                    print("-" * 30)
                            print(verde + "Horas totais:", soma, Fore.RESET, "\n")
                            input("Aperte 'enter' para voltar.")
                    
                    case "2":
                        meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
                        entrada = input("Digite o mês e o ano (Formato: maio-2024 ou 05-2024): ")
                        if entrada != "":
                            if "/" in entrada:
                                mes, ano = entrada.split("/")
                            elif "-" in entrada:
                                mes, ano = entrada.split("-") 
                            else:
                                mes, ano = None, None
                                print("Formato inválido.")
                                time.sleep(1)
                            if (mes != None and ano != None):
                                os.system("cls")
                                if mes in meses:
                                    mes_numero = meses.index(mes) + 1
                                    mes_numero = "0" + str(mes_numero)
                                elif mes == "marco":
                                    mes_numero = 3
                                    mes_numero = "0" + str(mes_numero)
                                elif mes.isdigit() and int(mes) in range(1,13):
                                    mes_numero = mes
                                mes_numero_formatado = str(mes_numero)
                                a = []
                                for num in demandas:
                                    a.append(num)
                                a.sort()
                                soma = 0
                                for num in a[::-1]:
                                    for data in demandas[num]["datas"]:
                                        dia_json,mes_json,ano_json = data.split("/")
                                        if mes_numero_formatado == mes_json and ano == ano_json:
                                            soma = soma + demandas[num]["datas"][data]
                                            print(f"{amarelo + num} - {demandas[num]['titulo'] + Fore.RESET}")
                                            print(azul + f"Horas registradas em {data}: {demandas[num]['datas'][data]}" + Fore.RESET)
                                            print("-" * 30)
                                print(verde + "Horas totais:", soma, Fore.RESET, "\n")
                                input("Aperte 'enter' para voltar.")
                    case "3":
                        periodo1,periodo2 = input("Digite um período (Formato: '01/01/2023-01/01/2024'): ").split("-")
                    
                    case "4"|"":
                        break
            
        
        case "4": # Exibir demandas ativas
            os.system("cls")      
            a = []
            for num in demandas:
                a.append(num)
            a.sort()
            for num in a[::-1]:
                soma = 0
                for item in demandas[num]["datas"].items():
                    soma = soma + int(item[1])
                diferenca = int(demandas[num]["estimativa"]) - soma
                if demandas[num]["status"] == "ativa":
                    lista_data = list(demandas[num]["datas"].items())
                    printar_demanda()
                    print("-" * 20)
            print()
            input("Aperte enter para voltar a tela principal.")
                            
        case "5": # Exibir demandas concluídas
            os.system("cls")
            a = []
            for num in demandas:
                a.append(num)
            a.sort()
            for num in a[::-1]:
                soma = 0
                for item in demandas[num]["datas"].items():
                    soma = soma + int(item[1])
                diferenca = int(demandas[num]["estimativa"]) - soma
                if demandas[num]["status"] == "concluida":
                    lista_data = list(demandas[num]["datas"].items())
                    printar_demanda()
                    print("-" * 20)
            print()
            input("Aperte enter para voltar a tela principal.")
        
        case "6": # Fechar programa
            os.system("cls")
            print("Salvando...")
            time.sleep(0.8)
            os.system("cls")
            print("Dados salvos.")
            time.sleep(0.5)
            print("Fechando programa...")
            time.sleep(1)
            break
