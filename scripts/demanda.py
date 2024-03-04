import os
import time
import json
from datetime import datetime

def status():
    if diferenca <= 0:
        status = "concluída"
    else:
        status = "ativa"
    return status


while True:
    demanda_numero = []
    demanda_titulo = []

    try:
        with open("demandas.json", 'r') as f:
            demandas = json.load(f)
            for numero in demandas:
                demanda_numero.append(numero)
                demanda_titulo.append(demandas[numero]["titulo"])
                
    except FileNotFoundError:
        demandas = {}
        with open("demandas.json", 'w') as f:
            json.dump(demandas, f, indent=4) 
    
    os.system("cls")
    print("1. Pesquisar demanda.\n2. Cadastrar/Editar demanda.\n3. Listar demandas em execução\n4. Listar demandas concluídas.\n5. Salvar e fechar programa.")
    principal_input = (input("> "))
    if  principal_input.isdigit():    
        match int(principal_input):
            
            case 1:  
                digitar_num_titulo = input("Digite o número ou o titulo da demanda: ")
                if digitar_num_titulo in demanda_numero or digitar_num_titulo in demanda_titulo:
                    os.system("cls")   
                    if not digitar_num_titulo.isdigit():
                        num = demanda_titulo.index(digitar_num_titulo)
                        num = demanda_numero[num]
                    else:
                        num = digitar_num_titulo
                    
                    lista = list(demandas[num]["datas"].items())
                    soma = 0
                    for item in lista:
                        soma = soma + int(item[1])
                    diferenca = int(demandas[num]['estimativa']) - soma             
                    while True:
                        os.system("cls")
                        print(f"{num} - {demandas[num]['titulo']}")
                        print(f"Estimativa: {demandas[num]['estimativa']}h")
                        print(f"Status: {status()}")
                        print(f"Horas gastas: {soma}h")
                        print(f"Horas restantes: {diferenca}h")
                        
                        print("\n1. Computar horas\n2. Ver detalhes\n3. Voltar (enter)")
                        input_horas_ver_detalhes = input("> ")
                        
                        
                        if input_horas_ver_detalhes == "1": # Computar horas
                            computar_horas = input("Digite as horas: ")
                            if computar_horas != "" and computar_horas.isdigit():
                                print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                                data_settings = input("> ")
                                
                                if data_settings == "1":
                                    data = datetime.now().date().strftime("%d/%m/%Y")
                                    computar_dict = {}
                                    computar_dict = {data: int(computar_horas)}
                                    demandas[num]["datas"].update(computar_dict)
                                    with open("demandas.json" , "w") as f:
                                        json.dump(demandas , f, indent=4)
                                    print("Horas computadas com sucesso!")
                                    time.sleep(1)
                                    break
                                
                                elif data_settings == "2":
                                    data_input = input("Digite a data (formato: dia/mes/ano): ")
                                    computar_dict = {}
                                    computar_dict = {data_input: int(computar_horas)}
                                    demandas[num]["datas"].update(computar_dict)
                                    with open("demandas.json" , "w") as f:
                                        json.dump(demandas , f, indent=4)
                                    print("Horas computadas com sucesso!")
                                    time.sleep(1)
                                    break
                            else:
                                print("Formato inválido.")
                                time.sleep(1)
                        
                        elif input_horas_ver_detalhes == "2": # Ver detalhes
                            os.system("cls")
                            lista = list(demandas[num]["datas"].items())
                            print(f"{num} - {demandas[num]['titulo']}")
                            print(f"Estimativa: {demandas[num]['estimativa']}h")
                            print(f"Status: {status()}")
                            print(f"Horas gastas: {soma}h")
                            print(f"Horas restantes: {diferenca}h") 
                            for item in lista:
                                print(f"{item[0]}: {item[1]}h")
                            
                            print("\n1. Computar horas\n2. Ver menos detalhes\n3. Voltar (enter)")
                            input_horas_ver_detalhes = input("> ")
                            
                            if input_horas_ver_detalhes == "1": # Computar horas
                                computar_horas = input("Digite as horas: ")
                                if computar_horas != "" and computar_horas.isdigit():
                                    print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                                    data_settings = input("> ")
                                    
                                    if data_settings == "1":
                                        data = datetime.now().date().strftime("%d/%m/%Y")
                                        computar_dict = {}
                                        computar_dict = {data: int(computar_horas)}
                                        demandas[num]["datas"].update(computar_dict)
                                        with open("demandas.json" , "w") as f:
                                            json.dump(demandas , f, indent=4)
                                        print("Horas computadas com sucesso!")
                                        time.sleep(1)
                                        break

                                    
                                    elif data_settings == "2":
                                        data_input = input("Digite a data (formato: dia/mes/ano): ")
                                        computar_dict = {}
                                        computar_dict = {data_input: int(computar_horas)}
                                        demandas[num]["datas"].update(computar_dict)
                                        with open("demandas.json" , "w") as f:
                                            json.dump(demandas , f, indent=4)
                                        print("Horas computadas com sucesso!")
                                        time.sleep(1)
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

            
            case 2:
                while True:
                    os.system("cls")
                    print("1. Adicionar demanda\n2. Remover demanda\n3. Editar demanda\n4. Voltar (enter)")
                    editar_input = input("> ")
                    match editar_input:
                        case "1":
                            os.system("cls")
                            print("Para voltar a qualquer momento aperte 'Enter'\n")
                            cadastrar_numero = input("Digite o NÚMERO da demanda: ")
                            
                            if cadastrar_numero != "" and cadastrar_numero not in demandas:
                                cadastrar_titulo = input("Digite o TÍTULO da demanda: ")
                                
                                if cadastrar_titulo != "":    
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
                                print("Não foi posssível cadastrar essa demanda (Há outra com o mesmo número registrada).")
                                time.sleep(3)
                        
                        case "2":
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
                        case "3":
                            editar_demanda = input("Digite o número da demanda que quer editar")
                            if editar_demanda not in demandas:
                                print("Demanda não encontrada")
                            else:
                                print("Estou trabalhando nessa funcionalidade. ;)")
                                time.sleep(3)
                        
                        case "":
                            break

                    
            
            
            case 3:
                os.system("cls")
                
                for num in demandas:
                    soma = 0
                    for item in demandas[num]["datas"].items():
                        soma = soma + int(item[1])
                    diferenca = int(demandas[num]["estimativa"]) - soma
                    if diferenca > 0:
                        lista = list(demandas[num]["datas"].items())
                        print(f"{num} - {demandas[num]['titulo']}")
                        print(f"Estimativa: {demandas[num]['estimativa']}h")
                        print(f"Status: ativa")
                        print(f"Horas gastas: {soma}h")
                        print(f"Horas restantes: {diferenca}h")
                        print("-" * 20)
                print()
                input("Aperte enter para voltar a tela principal.")
                             
            case 4:
                os.system("cls")
                for num in demandas:
                    soma = 0
                    for item in demandas[num]["datas"].items():
                        soma = soma + int(item[1])
                    diferenca = int(demandas[num]["estimativa"]) - soma
                    if diferenca <= 0:
                        lista = list(demandas[numero]["datas"].items())
                        print(f"{num} - {demandas[num]['titulo']}")
                        print(f"Estimativa: {demandas[num]['estimativa']}h")
                        print(f"Status: concluída")
                        print(f"Horas gastas: {soma}h")
                        print(f"Horas restantes: {diferenca}h")
                        print("-" * 20)
                print()
                input("Aperte enter para voltar a tela principal.")
            case 5:
                os.system("cls")
                print("Salvando...")
                time.sleep(0.8)
                os.system("cls")
                print("Dados salvos.")
                time.sleep(.5)
                print("Fechando programa...")
                time.sleep(1)
                break