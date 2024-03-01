# salvar: numemro da demanda, titulo da demandda, estimativa, 
import os
import time

demanda = []
demanda_concluida = []
demanda_ativa = []
demanda_numero = ["davi"]
demanda_titulo = ["011"]
 
while True:
    
    os.system("cls")
    print("1. Pesquisar demanda.\n2. Cadastrar demanda.\n3. Listar demandas em execução\n4. Listar demandas concluídas.")
    principal_input = (input("> "))
    if  principal_input.isdigit():    
        match int(principal_input):
            
            case 1:
                
                
                digitar_num_titulo = input("Digite o número ou o titulo da demanda: ")
                if digitar_num_titulo in demanda_numero or digitar_num_titulo in demanda_titulo:
                    os.system("cls")   
                    print("00001 - Demanda titulo\nEstimativa: 0h\nHoras concluidas: 0h\nHoras restantes: 0h\n")
                    print("1. Computar horas\n2. Ver detalhes\n3. Voltar (enter)")
                    input_horas_ver_detalhes = input("> ")
                    
                    
                    if input_horas_ver_detalhes == "1":
                        computar_horas = input("Digite as horas: ")
                        data_settings = input("1. Usar data automatica\n2. Digitar data manualmente\n3. Cancelar (enter)")
                    
                    
                    elif input_horas_ver_detalhes == "2":
                        os.system("cls")
                        print("demandas detalhada")
                        voltar = input("Aperte enter para voltar a tela principal.")
                
                
                else:                
                    print("Demanda não encontrada.")
                    time.sleep(1)

            case 2:
                cadastrar_numero = int(input("Digite o número da demanda: "))
                cadastrar_titulo = input("Digite o titulo da demanda: ")
                cadastrar_estimativa = float(input("Digite a estimativa de horas da demanda: "))
            case 3:
                ...
            case 4:
                ...