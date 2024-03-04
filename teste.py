import os
import time
import json
#from datetime import datetime

""" def status():
    if diferenca <= 0:
        status = "concluída"
    else:
        status = "ativa"
    return status
 """

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
                        remover_demanda = input("Digite o número da demanda que deseja remover: ")
                        if remover_demanda not in demandas:
                            print("Demanda não encontrada.")
                        else:
                            print(f"Você realmente deseja excluir a demanda {remover_demanda} (s/n)")
                            confirmacao = input("> ")
                            if confirmacao.upper() == "S":
                                del demandas[remover_demanda]
                                with open("demandas.json" , "w") as f:
                                    json.dump(demandas , f, indent=4)
                                print(f"Demanda {remover_demanda} excluída com sucesso.")
                                time.sleep(1)
