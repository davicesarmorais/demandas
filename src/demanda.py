import os
import time
import json
from datetime import datetime, timedelta
from colorama import init, Fore
init()

#cores -------------------
verde = Fore.GREEN
azul = Fore.LIGHTBLUE_EX
amarelo = Fore.YELLOW
red = Fore.LIGHTRED_EX
roxo = Fore.LIGHTMAGENTA_EX
# ------------------------

def salvar_horas(data,soma):
    computar_dict = {}
    computar_dict = {data: int(computar_horas) + soma}
    demandas[num]["datas"].update(computar_dict)
    with open("demandas.json" , "w") as f:
        json.dump(demandas , f, indent=4)
    print("\033[1;32mHoras computadas com sucesso!\033[m")
    time.sleep(0.8)

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
        while True:
            try:
                data = input("Digite a data (formato: dd/mm/yyyy): ")
                if data == "":
                    break
                else:
                    data = datetime.strptime(data, "%d/%m/%Y")
                    data = data.strftime("%d/%m/%Y")
                    break
            except ValueError:
                print("\033[1;31mFormato inválido\033[m")
    
    if data != "":
        if data in demandas[num]["datas"]:
            salvar_horas(data, demandas[num]["datas"][data])
        else:
            salvar_horas(data, 0)

def settings_data():
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
    print(f"{'{ Demandas }':-^80}")
    for numero in demandas:
        print(f"{numero} - {demandas[numero]['titulo']}")
    if not demandas:
        print("\033[3mNenhuma demanda registrada.\033[m")
    print("-" * 80)
    print("\n[?] - Ajuda",
          "\n1. Pesquisar demanda",
          "\n2. Cadastrar/Editar demanda",
          "\n3. Ver relatórios de apontamentos",
          "\n4. Listar demandas em execução",
          "\n5. Listar demandas concluídas",
          "\n6. Salvar e fechar programa",)
    principal_input = (input("> "))
    match principal_input:
        
        case "1":  # Pesquisar demandas
            digitar_num_titulo = input("\033[1mDigite o número ou o titulo da demanda: \033[m")
            if digitar_num_titulo != "":
                if digitar_num_titulo not in demanda_numero and digitar_num_titulo not in demanda_titulo:
                    print("\033[1;31mDemanda não encontrada.\033[m")
                    time.sleep(1)          
                
                else:
                    while True: 
                        if not digitar_num_titulo.isdigit(): # se nao for um numero (numero da demanda) puxa o valor do titulo por meio de indexagem do numeri
                            num = demanda_numero[demanda_titulo.index(digitar_num_titulo)]
                        else:
                            num = digitar_num_titulo
                        lista_data = list(demandas[num]["datas"].items()) # datas vao para uma lista par melhor menipulação
                        soma = 0
                        for item in lista_data:
                            soma = soma + int(item[1]) # soma de horas gastas
                        diferenca = int(demandas[num]['estimativa']) - soma  # horas restantes         
                        
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
                                if computar_horas != '':
                                    if computar_horas.isdigit():
                                        settings_data()
                                    else:
                                        print("\033[3;31mFormato inválido.\033[m")
                                        time.sleep(1)  
                                
                            case "2":
                                if demandas[num]["status"] == "ativa":
                                    print("\033[1;34mVocê deseja marcar essa demanda como\033[m \033[1;32mconcluída?\033[m \033[1;34m(s/n)\033[m")
                                    decisao = input("> ")
                                    if decisao.upper() == "S":
                                        demandas[num]["status"] = "concluida"
                                        atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                    else:
                                        print("\033[1;34mOperação cancelada.\033[m")
                                        time.sleep(1.5)

                                elif demandas[num]["status"] == "concluida":
                                    print("\033[1;34mVocê deseja marca essa demanda como\033[m \033[1;32mativa?\033[m \033[1;34m(s/n)\033[m")
                                    decisao = input("> ")
                                    if decisao.upper() == "S":
                                        demandas[num]["status"] = "ativa"
                                        atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                    else:
                                        print("\033[1;34mOperação cancelada.\033[m")
                                        time.sleep(1.5)
                            
                            case "3"|"": # voltar
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
                        print("\033[3mPara cancelar a qualquer momento digite 'cancel'\033[m\n")
                        
                        def cadastrar():
                            while True:
                                os.system("cls")
                                print("\033[3mPara cancelar a qualquer momento digite 'cancel'\033[m\n")
                                cadastrar_numero = input("Digite o NÚMERO da demanda: ")
                                if cadastrar_numero == "cancel":
                                    return  
                                if cadastrar_numero in demandas:
                                    print("\033[1;31mNúmero já registrado.\033[m")
                                    time.sleep(1)
                                else:
                                    break
                                
                            cadastrar_titulo = input("Digite o TÍTULO da demanda: ")
                            if cadastrar_titulo == "cancel":
                                return
                            
                            while True:
                                cadastrar_estimativa = input("Digite a estimativa de horas da demanda: ")
                                if cadastrar_estimativa == "cancel":
                                    return
                                if not cadastrar_estimativa.isdigit():
                                    print("\033[3;31mFormato inválido.\033[m")
                                    time.sleep(1)
                                else:
                                    break
                               
                            cadastro_dict = {}
                            cadastro_dict[cadastrar_numero] = {"titulo": cadastrar_titulo, "estimativa": int(cadastrar_estimativa), "status": "ativa", "datas": {}}
                            demandas.update(cadastro_dict)
                            atualizar_demanda(None, False) # atualizar lista
                            print(f"\033[1;32mDemanda ({cadastrar_numero}) adicionada com sucesso!\033[m")
                            time.sleep(2) 
                            
                        cadastrar()
                    
                    case "2": # Remover demanda
                        os.system('cls')
                        print(f"{'{ Demandas }':-^80}")
                        for numero in demandas:
                            print(f"{numero} - {demandas[numero]['titulo']}")
                        if not demandas:
                            print("\033[3mNenhuma demanda registrada.\033[m")
                        print("-" * 80)
                        remover_demanda = input("Digite o número da demanda que deseja remover: ")
                        if remover_demanda != "":
                            if remover_demanda not in demandas:
                                print("\033[1;31mDemanda não encontrada.\033[m")
                                time.sleep(1.5)
                            else:
                                print(f"\033[1;34mVocê realmente deseja excluir a demanda {remover_demanda}? (s/n)\033[m")
                                confirmacao = input("> ")
                                if confirmacao.upper() == "S":
                                    del demandas[remover_demanda]
                                    atualizar_demanda(None, False)
                                    print(f"\033[1;32mDemanda {remover_demanda} excluída com sucesso.\033[m")
                                    time.sleep(1)
                                else:
                                    print("\033[1;34mOperação cancelada.\033[m")
                                    time.sleep(1.5)
                    
                    case "3": # Editar demanda
                        os.system('cls')
                        print(f"{'{ Demandas }':-^80}")
                        for numero in demandas:
                            print(f"{numero} - {demandas[numero]['titulo']}")
                        if not demandas:
                            print("\033[3mNenhuma demanda registrada.\033[m")
                        print("-" * 80)
                        editar_demanda = input("Digite o número da demanda que quer editar: ")
                        if editar_demanda != "":
                            if editar_demanda not in demandas:
                                print("\033[1;34mDemanda não encontrada\033[m")
                                time.sleep(1)
                            else:
                                os.system("cls")
                                a = demandas[editar_demanda]
                                lista_data = list(demandas[editar_demanda]["datas"].items())
                                print(amarelo + f"{editar_demanda}: {a['titulo']}" + Fore.RESET)
                                print(f"Estimativa: {roxo}{a['estimativa']}h{Fore.RESET}")
                                for data in lista_data:
                                    print(f"{data[0]}: {data[1]}h")
                                print("\nDigite qual a informação que deseja alterar \033[3m(Ex: 'numero', 'titulo', 'estimativa', 'data', 'hora')\033[m")
                                escolher_info = input("> ")                    
                                match escolher_info.lower():
                                
                                    case "titulo"|"título": # Editar titulo
                                        editar_titulo = input("Digite o novo nome do titulo: ")
                                        if editar_titulo != "":
                                            print(f"\033[1;34mVocê deseja confirmar a alteração para '{editar_titulo}'? (s/n)\033[m")
                                            choice = input("> ")
                                            if choice.upper() == "S":
                                                demandas[editar_demanda]["titulo"] = editar_titulo
                                                atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                                break
                                            else:
                                                print("\033[1;34mOperação cancelada.\033[m")
                                                time.sleep(1.5)
                                                

                                    case "estimativa": # Editar estimativa
                                        editar_estimativa = input("Digite a nova quantidade de horas de estimativa: ")
                                        if editar_estimativa != "":
                                            print(f"\033[1;34mVocê deseja confirmar a alteração para {editar_estimativa}h? (s/n)\033[m")
                                            choice = input("> ")
                                            if choice in ["s", "S"] and editar_estimativa.isdigit():
                                                demandas[editar_demanda]["estimativa"] = int(editar_estimativa)
                                                atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                                break
                                            else:
                                                print("\033[1;34mOperação cancelada.\033[m")
                                                time.sleep(1.5)

                                    case "data"|"datas"|"horas"|"hora": # Editar data, horas
                                        editar_data = input("Digite a data que quer editar, excluir ou modificar horas: ")
                                        if editar_data == "" or editar_data not in demandas[editar_demanda]["datas"]:
                                            print("\033[1;34mOperação cancelada.\033[m")
                                            time.sleep(1.5)
                                        
                                        else:
                                            print("1. Mudar data\n2. Mudar horas\n3. Exluir data\n4. Voltar (enter)")
                                            choice2 = input("> ")
                                            match choice2:
                                                
                                                case "1": # Editar data
                                                    while True:
                                                        try:
                                                            trocar_data = input("Digite a nova data. Formato: (dd/mm/yyyy): ")
                                                            if trocar_data == "":
                                                                print("\033[1;34mOperação cancelada.\033[m")
                                                                time.sleep(1)
                                                                break
                                                            else:
                                                                trocar_data = datetime.strptime(trocar_data, "%d/%m/%Y")
                                                                trocar_data = trocar_data.strftime("%d/%m/%Y")
                                                                break
                                                        except ValueError:
                                                            print("\033[1;31mFormato inválido\033[m")
                                                        
                                                    if trocar_data != "":
                                                            
                                                        print(f"\033[1;34mVocê deseja confirmar a alteração para '{trocar_data}'? (s/n)\033[m")
                                                        choice = input("> ")
                                                        if choice in ["s", "S"]:
                                                            if trocar_data in demandas[editar_demanda]["datas"]:
                                                                valor = demandas[editar_demanda]["datas"][editar_data] + demandas[editar_demanda]["datas"][trocar_data]
                                                                demandas[editar_demanda]["datas"][trocar_data] = valor
                                                                del demandas[editar_demanda]["datas"][editar_data]
                                                                atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                                                break
                                                                
                                                            else:
                                                                x = demandas[editar_demanda]["datas"][editar_data]
                                                                del demandas[editar_demanda]["datas"][editar_data]
                                                                demandas[editar_demanda]["datas"][trocar_data] = x
                                                                atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                                                break
                                                        else:
                                                            print("\033[1;34mOperação cancelada.\033[m")
                                                            time.sleep(1.5)
                                                
                                                case "2": # Editar horas
                                                    escolha_horas = input("Digite a nova quantidade de horas: ")
                                                    if escolha_horas != "" and escolha_horas.isdigit():
                                                        print(f"\033[1;34mVocê tem certeza que quer alterar as horas para {escolha_horas}h? (s/n)\033[m")
                                                        certeza = input("> ")
                                                        if certeza.upper() == "S":
                                                            demandas[editar_demanda]["datas"][editar_data] = int(escolha_horas)
                                                            atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True)
                                                            break
                                                        else:
                                                            print("\033[1;34mOperação cancelada.\033[m")
                                                            time.sleep(1.5)
                                                    else:
                                                        print("\033[1;34mOperação cancelada.\033[m")
                                                        time.sleep(1.5)
                                                
                                                case "3": # Excluir data
                                                    print(f"\033[1;34mVocê tem certeza que quer excluir a data {editar_data} da demanda {editar_demanda}? (s/n)\033[m")
                                                    choice3 = input("> ")
                                                    if choice3.upper() == "S":
                                                        del demandas[editar_demanda]["datas"][editar_data]
                                                        atualizar_demanda('\033[1;32mData excluída com sucesso!\033[m', True)
                                                        break
                                                    else:
                                                        print("\033[1;34mOperação cancelada.\033[m")
                                                        time.sleep(1.5)
                            
                                    case "numero"|"número": # Editar numero demanda
                                        escolha_numero = input("Digite o novo número da demanda: ")
                                        if escolha_numero != ""and escolha_numero not in demandas:
                                            print(f"\033[1;34mVocê tem certeza que deseja alterar o número dessa demanda para {escolha_numero}? (s/n)\033[m")
                                            decisao = input("> ")
                                            if decisao.upper() == "S":
                                                x = demandas[editar_demanda]
                                                del demandas[editar_demanda]
                                                demandas[escolha_numero] = x
                                                atualizar_demanda("\033[1;32mDemanda atualizada com sucesso!\033[m", True) 
                                            else:

                                                print("\033[1;34mOperação cancelada.\033[m")
                                                time.sleep(1.5)
                                        else:
                                            print("\033[1;34mOperação cancelada ou número já registrado.\033[m")
                                            time.sleep(1)
                                                                
        case "3": # Relatórios
            while True:
                os.system('cls')
                print("1. Data específica\n2. Mês específico\n3. Período\n4. Voltar (enter)")
                relatorio_input = input("> ")
                match relatorio_input:
                    case "4"|"":
                        break
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
                            input("\033[1mAperte 'enter' para voltar.\033[m")
                    
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
                                print("\033[1;31mFormato inválido.\033[m")
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
                                            print(azul + f"Horas registradas em {data}: {demandas[num]['datas'][data]}h" + Fore.RESET)
                                            print("-" * 30)
                                print(verde + "Horas totais:", soma, Fore.RESET, "\n")
                                input("\033[1mAperte 'enter' para voltar.\033[m")
                    case "3":
                        try:
                            periodo1,periodo2 = input("Digite um período (Formato: '01/01/2023-01/01/2024'): ").split("-")
                            dia1,mes1,ano1 = periodo1.split("/")
                            dia2,mes2,ano2 = periodo2.split("/")
                            data_inicial = datetime(int(ano1), int(mes1), int(dia1))
                            data_final = datetime(int(ano2), int(mes2), int(dia2))
                            passo = timedelta(days=1)
                            datas_range = []
                            while data_inicial <= data_final:
                                datas_range.append(data_inicial.strftime("%d/%m/%Y"))
                                data_inicial += passo
                            a = []
                            for num in demandas:
                                a.append(num)
                            a.sort()
                            soma = 0
                            os.system('cls')
                            for num in a[::-1]:
                                for data in demandas[num]["datas"]:
                                    if data in datas_range:
                                        soma = soma + demandas[num]["datas"][data]
                                        print(amarelo + f"{num} - {demandas[num]['titulo']}" + Fore.RESET)
                                        print(azul + f"Horas registradas em {data}: {demandas[num]['datas'][data]}" + Fore.RESET)
                                        print("-" * 30)
                            print(verde + "Horas torais:", soma, Fore.RESET, "\n")
                            input("\033[1mAperte 'enter' para voltar.\033[m")

                        except ValueError:
                            print("\033[1;31mFormato inválido ou operação cancelada.\033[m")
                            time.sleep(1)
                    
                    
            
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
            input("\033[1mAperte enter para voltar a tela principal.\033[m")
                            
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
            input("\033[1mAperte enter para voltar a tela principal.\033[m")
        
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
        
        case "?":
            os.system('cls')
            print("Para obter ajuda confira o README no github com todas as funções explicadas.")
            print("\nhttps://github.com/davicesarmorais/demandas/blob/main/README.md\n")
            input("\033[1mAperte 'enter' para voltar.\033[m")