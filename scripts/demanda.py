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

def status():
    if diferenca <= 0:
        status = verde + "concluída" + Fore.RESET
    else:
        status = azul + "ativa" + Fore.RESET
    return status

def salvar_horas(data,soma):
    computar_dict = {}
    computar_dict = {data: int(computar_horas) + soma}
    demandas[num]["datas"].update(computar_dict)
    with open("demandas.json" , "w") as f:
        json.dump(demandas , f, indent=4)
    print("Horas computadas com sucesso!")
    time.sleep(1)

def atualizar_demanda(texto):
    with open("demandas.json", "w") as f:
        json.dump(demandas, f, indent=4)
    print(texto)
    time.sleep(1)

def printar_demanda():
    print(amarelo + f"{num} - {demandas[num]['titulo']}" + Fore.RESET)
    print(f"Estimativa: {roxo}{demandas[num]['estimativa']}h{Fore.RESET}")
    print(f"Status: {status()}")
    print(f"Horas gastas: {verde}{soma}h{Fore.RESET}")
    print(f"Horas restantes: {red}{diferenca}h{Fore.RESET}")

while True: # loop principal
    demanda_numero = [] # sempre recomeçar vazio para nâo dar erro
    demanda_titulo = []

    try:
        with open("demandas.json", 'r') as f: # abrir json e mandar demanda_numero e demanda_titulo para  lista
            demandas = json.load(f)
            for numero in demandas:
                demanda_numero.append(numero)
                demanda_titulo.append(demandas[numero]["titulo"])
                
    except FileNotFoundError: # cria arquivo json se nao existir
        demandas = {}
        with open("demandas.json", 'w') as f:
            json.dump(demandas, f, indent=4) 
    
    os.system("cls")
    print("1. Pesquisar demanda.\n2. Cadastrar/Editar demanda.\n3. Listar demandas em execução\n4. Listar demandas concluídas.\n5. Salvar e fechar programa.")
    principal_input = (input("> "))
    if  principal_input.isdigit():    
        match int(principal_input):
            
            case 1:  # Pesquisar demandas
                digitar_num_titulo = input("Digite o número ou o titulo da demanda: ")
                if digitar_num_titulo in demanda_numero or digitar_num_titulo in demanda_titulo:
                    os.system("cls")   
                    if not digitar_num_titulo.isdigit(): # se nao for um numero (numero da demanda) puxa o valor do titulo por meio de indexagem do numeri
                        num = demanda_titulo.index(digitar_num_titulo) 
                        num = demanda_numero[num]
                    else:
                        num = digitar_num_titulo
                    
                    lista = list(demandas[num]["datas"].items()) # datas vao para uma lista par melhor menipulação
                    soma = 0
                    for item in lista:
                        soma = soma + int(item[1]) # soma de horas gastas
                    diferenca = int(demandas[num]['estimativa']) - soma  # horas restantes       
                    while True: 
                        os.system("cls")
                        printar_demanda()              
                        print("\n1. Inputar horas\n2. Ver detalhes\n3. Voltar (enter)")
                        input_horas_ver_detalhes = input("> ")
                        
                        
                        if input_horas_ver_detalhes == "1": # Computar horas (- detalhes)
                            computar_horas = input("Digite as horas: ")
                            if computar_horas != "" and computar_horas.isdigit():
                                print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                                data_settings = input("> ")
                                
                                if data_settings == "1": # data auto (- detalhes)
                                    data = datetime.now().date().strftime("%d/%m/%Y")
                                    if data in demandas[num]["datas"]:
                                        salvar_horas(data, demandas[num]["datas"][data])
                                        break
                                    else:
                                        salvar_horas(data, 0)
                                        break
                            
                                elif data_settings == "2": # data manual (- detalhes)
                                    data_input = input("Digite a data (formato: dia/mes/ano): ")
                                    if data_input in demandas[num]["datas"]:
                                        salvar_horas(data_input, demandas[num]["datas"][data])
                                        break    
                                    else:
                                        salvar_horas(data_input, 0)
                                        break
                            else:
                                print("Formato inválido.")
                                time.sleep(1)
                        
                        elif input_horas_ver_detalhes == "2": # Ver detalhes
                            os.system("cls")
                            lista = list(demandas[num]["datas"].items())
                            printar_demanda() 
                            for item in lista:
                                print(f"{item[0]}: {item[1]}h")
                            print("\n1. Inputar horas\n2. Ver menos detalhes\n3. Voltar (enter)")
                            input_horas_ver_detalhes = input("> ")
                            
                            if input_horas_ver_detalhes == "1": # Computar horas (+ detalhes)
                                computar_horas = input("Digite as horas: ")
                                if computar_horas != "" and computar_horas.isdigit():
                                    print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                                    data_settings = input("> ")
                                    
                                    if data_settings == "1": # data auto (+ detalhes)
                                        data = datetime.now().date().strftime("%d/%m/%Y")
                                        if data in demandas[num]["datas"]:
                                            salvar_horas(data, demandas[num]["datas"][data])
                                            break
                                        else:
                                            salvar_horas(data, 0)
                                            break
                                
                                    elif data_settings == "2": # data manual (+ detalhes)
                                        data_input = input("Digite a data (formato: dia/mes/ano): ")
                                        if data_input in demandas[num]["datas"]:
                                            salvar_horas(data_input, demandas[num]["datas"][data])
                                            break    
                                        else:
                                            salvar_horas(data_input, 0)
                                            break
                                else:
                                    print("Formato inválido.")
                                    time.sleep(1)
                            
                            elif input_horas_ver_detalhes == "2": # ver menos detalhes
                                os.system("cls")
                            else:
                                break
                        else:
                            break
                
                else:                
                    print("Demanda não encontrada.")
                    time.sleep(1)

            
            case 2: # Editar demandas principal
                while True:
                    os.system("cls")
                    print("1. Adicionar demanda\n2. Remover demanda\n3. Editar demanda\n4. Voltar (enter)")
                    editar_input = input("> ")
                    match editar_input:
                        
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
                                        cadastro_dict[cadastrar_numero] = {"titulo": cadastrar_titulo, "estimativa": int(cadastrar_estimativa), "datas": {}}
                                        demandas.update(cadastro_dict)
                                        with open("demandas.json" , "w") as f:
                                            json.dump(demandas , f, indent=4) # atualizar lista
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
                                        with open("demandas.json" , "w") as f:
                                            json.dump(demandas , f, indent=4)
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
                                lista = list(demandas[editar_demanda]["datas"].items())
                                print(f"{editar_demanda}: {a['titulo']}")
                                print(f"Estimativa: {a['estimativa']}h")
                                for data in lista:
                                    print(f"{data[0]}: {data[1]}h")
                                print("\nDigite qual a informação que deseja alterar (Ex: 'numero', 'titulo', 'estimativa', 'data', 'hora')")
                                escolher_info = input("> ")
                                
                                
                                if escolher_info == "titulo": # Editar titulo
                                    editar_titulo = input("Digite o novo nome do titulo: ")
                                    if editar_titulo != "":
                                        print(f"Você deseja confirmar a alteração para '{editar_titulo}'? (s/n)")
                                        choice = input("> ")
                                        if choice.upper() == "S":
                                            demandas[editar_demanda]["titulo"] = editar_titulo
                                            atualizar_demanda("Demanda atualizada com sucesso!")
                                            break

                                elif escolher_info == "estimativa": # Editar estimativa
                                    editar_estimativa = input("Digite a nova quantidade de horas de estimativa: ")
                                    if editar_estimativa != "":
                                        print(f"Você deseja confirmar a alteração para {editar_estimativa}h? (s/n)")
                                        choice = input("> ")
                                        if choice in ["s", "S"] and editar_estimativa.isdigit():
                                            demandas[editar_demanda]["estimativa"] = int(editar_estimativa)
                                            atualizar_demanda("Demanda atualizada com sucesso!")
                                            break
                                        else:
                                            os.system("cls")
                                            print("Operação cancelada.")
                                            time.sleep(1.5)

                                elif escolher_info in ["data", "datas", "horas", "hora"]: # Editar data, horas
                                    editar_data = input("Digite a data que quer editar, excluir ou modificar horas: ")
                                    if editar_data != "" and editar_data in demandas[editar_demanda]["datas"]:
                                        print("1. Mudar data\n2. Mudar horas\n3. Exluir data\n4. Voltar (enter)")
                                        choice2 = input("> ")
                                        match choice2:
                                            
                                            case "1": # Editar data
                                                trocar_data = input("Digite a nova data. Formato: (dia/mes/anos): ")
                                                print(f"Você deseja confirmar a alteração para '{trocar_data}'? (s/n)")
                                                choice = input("> ")
                                                if choice in ["s", "S"]:
                                                    x = demandas[editar_demanda]["datas"][editar_data]
                                                    del demandas[editar_demanda]["datas"][editar_data]
                                                    demandas[editar_demanda]["datas"][trocar_data] = x
                                                    atualizar_demanda("Demanda atualizada com sucesso!")
                                                    break
                                            
                                            case "2": # Editar horas
                                                escolha_horas = input("Digite a nova quantidade de horas: ")
                                                if escolha_horas != "" and escolha_horas.isdigit():
                                                    certeza = input(f"Você tem certeza que quer alterar as horas para {escolha_horas}h? (s/n): ")
                                                    if certeza.upper() == "S":
                                                        demandas[editar_demanda]["datas"][editar_data] = int(escolha_horas)
                                                        atualizar_demanda("Demanda atualizada com sucesso!")
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
                                                    atualizar_demanda('Data excluída com sucesso!')
                                                    break
                                    else:
                                        os.system("cls")
                                        print("Operação cancelada")
                                        time.sleep(1.5)
                                
                                elif escolher_info == "numero": # Editar numero demanda
                                    escolha_numero = input("Digite o novo número da demanda: ")
                                    if escolha_numero != ""and escolha_numero not in demandas:
                                        print(f"Você tem certeza que deseja alterar o número dessa demanda para {escolha_numero}? (s/n)")
                                        decisao = input("> ")
                                        if decisao.upper() == "S":
                                            x = demandas[editar_demanda]
                                            del demandas[editar_demanda]
                                            demandas[escolha_numero] = x
                                            atualizar_demanda("Demanda atualizada com sucesso!") 
                                    else:
                                        print("Operação cancelada ou número já registrado.")
                                        time.sleep(1)
                                                                   
                        case "":
                            break
 
            case 3: # Exibir demandas ativas
                os.system("cls")      
                for num in demandas:
                    soma = 0
                    for item in demandas[num]["datas"].items():
                        soma = soma + int(item[1])
                    diferenca = int(demandas[num]["estimativa"]) - soma
                    if diferenca > 0:
                        lista = list(demandas[num]["datas"].items())
                        printar_demanda()
                        print("-" * 20)
                print()
                input("Aperte enter para voltar a tela principal.")
                             
            case 4: # Exibir demandas concluídas
                os.system("cls")
                for num in demandas:
                    soma = 0
                    for item in demandas[num]["datas"].items():
                        soma = soma + int(item[1])
                    diferenca = int(demandas[num]["estimativa"]) - soma
                    if diferenca <= 0:
                        lista = list(demandas[num]["datas"].items())
                        printar_demanda()
                        print("-" * 20)
                print()
                input("Aperte enter para voltar a tela principal.")
           
           
            case 5: # Fechar programa
                os.system("cls")
                print("Salvando...")
                time.sleep(0.8)
                os.system("cls")
                print("Dados salvos.")
                time.sleep(0.5)
                print("Fechando programa...")
                time.sleep(1)
                break