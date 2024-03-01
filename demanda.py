# salvar: numemro da demanda, titulo da demandda, estimativa, 
import os

demanda = []
demanda_concluida = []
demanda_ativa = []
demanda_numero = ["davi"]
demanda_titulo = ["011"]
 
print("1. Pesquisar demanda.\n2. Cadastrar demanda.\n3. Listar demandas em execução\n4. Listar demandas concluídas.")
principal_input = int(input("> "))
match principal_input:
    case 1:
        digitar_num_titulo = input("Digite o número ou o titulo da demanda: ")
        if digitar_num_titulo in demanda_numero or digitar_num_titulo in demanda_titulo:
            os.system("cls")   
            print("00001 - Demanda titulo\nEstimativa: 0h\nHoras concluidas: 0h\nHoras restantes: 0h")
        else:
            print("Demanda não encontrada.")

    case 2:
        cadastrar_numero = int(input("Digite o número da demanda: "))
        cadastrar_titulo = input("Digite o titulo da demanda: ")
        cadastrar_estimativa = float(input("Digite a estimativa de horas da demanda: "))
    case 3:
        ...
    case 4:
        ...