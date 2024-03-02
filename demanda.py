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
    print("1. Pesquisar demanda.\n2. Cadastrar demanda.\n3. Listar demandas em execução\n4. Listar demandas concluídas.")
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
                    
                    print(f"{num} - {demandas[num]['titulo']}")
                    print(f"Estimativa: {demandas[num]['estimativa']}h")
                    print(f"Status: {status()}")
                    print(f"Horas gastas: {soma}h")
                    print(f"Horas restantes: {diferenca}h")
                    
                    print("\n1. Computar horas\n2. Ver detalhes\n3. Voltar (enter)")
                    input_horas_ver_detalhes = input("> ")
                    
                    
                    if input_horas_ver_detalhes == "1": # Computar horas
                        computar_horas = input("Digite as horas: ")
                        print("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                        data_settings = input("> ")
                        
                        if data_settings == "1":
                            data = datetime.now().date().strftime("%d/%m/%Y")
                            computar_dict = {}
                            computar_dict = {data: int(computar_horas)}
                            demandas[num]["datas"].update(computar_dict)
                            with open("demandas.json" , "w") as f:
                                json.dump(demandas , f, indent=4)
                        
                        elif data_settings == "2":
                            data_input = input("Digite a data (formato: dia/mes/ano): ")
                            computar_dict = {}
                            computar_dict = {data_input: int(computar_horas)}
                            demandas[num]["datas"].update(computar_dict)
                            with open("demandas.json" , "w") as f:
                                json.dump(demandas , f, indent=4)
                    
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
                        print()
                        voltar = input("Aperte enter para voltar a tela principal.")
                
                
                else:                
                    print("Demanda não encontrada.")
                    time.sleep(1)

            
            case 2:
                os.system("cls")
                print("1. Adicionar demanda\n2. Remover demanda\n3. Editar demanda\n4. Voltar (enter)")
                editar_demanda = input("> ")
                match editar_demanda:
                    case "1":
                        os.system("cls")
                        print("Para voltar a qualquer momento aperte 'Enter'\n")
                        
                        cadastrar_numero = input("Digite o NÚMERO da demanda: ")
                        if cadastrar_numero != "":
                            
                            cadastrar_titulo = input("Digite o TÍTULO da demanda: ")
                            if cadastrar_titulo != "":
                                
                                cadastrar_estimativa = int(input("Digite a estimativa de horas da demanda: "))
                                if str(cadastrar_estimativa) != "":
                                    
                                    if cadastrar_numero not in demandas:
                                        cadastro_dict = {}
                                        cadastro_dict[cadastrar_numero] = {"titulo": cadastrar_titulo, "estimativa": cadastrar_estimativa, "datas": {}}
                                        demandas.update(cadastro_dict)
                                        with open("demandas.json" , "w") as f:
                                            json.dump(demandas , f, indent=4) # atualizar lista
                                        print(f"Demanda ({cadastrar_numero}) adicionada com sucesso!")
                                        time.sleep(2)
                                    
                                    else:
                                        print("Não foi posssível cadastrar essa demanda (Há outra com o mesmo número registrada).")
                                        time.sleep(3)
                    case "2":
                        print("funcao indisponivel no momentos")
                      #  remover_numero = input("Digite o número da demanda que deseja remover: ")
                    
            
            
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
                voltar = input("Aperte enter para voltar a tela principal.")
                             
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
                voltar = input("Aperte enter para voltar a tela principal.")