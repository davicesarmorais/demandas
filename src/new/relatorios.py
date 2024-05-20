from lib.lib import *
import re
from datetime import datetime


def formatar_mes_e_ano(entrada_data: str):
    formatos_aceitos = ["%m", "%m/%y", "%m/%Y", "%m%y", "%m%Y", "%m-%y", "%m-%Y"]
    ano_atual = datetime.now().strftime("%Y")
    
    for idx, formato in enumerate(formatos_aceitos):
        try:
            data = datetime.strptime(entrada_data, formato)
        except ValueError:
            continue
              
        if idx == 0:
            data = datetime.strftime(data, f"%m/{ano_atual}")
        else:
            data = data.strftime("%m/%Y")    
        
        return data
    
    else:
        print(f"{red}Formato inválido{reset}")
        return "formato invalido"


def mes_nome_para_numero(data: str) -> str:
    meses = {"janeiro": "01", "fevereiro": "02", "março": "03", "marco": "03",
             "abril": "04", "maio": "05", "junho": "06", "julho": "07", "agosto": "08",
             "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"}
    
    for mes in meses:
        if mes in data:
            mes_num = meses.get(mes)
            break
    else:
        return data
            
    return re.sub(mes, mes_num, data)


def converter_data(data_string) -> datetime:
    return datetime.strptime(data_string, "%d/%m/%Y")


def criar_dict_datas(checar_mes_contido: bool, 
                     entrada_data: str = None,
                     dt_inicial: datetime = None,
                     dt_final: datetime = None
                     ) -> dict | int:
    
    novo_dicionario = {}
    total_horas = 0
    for num, valor in demandas.items():
        for data, qtd_horas in valor["datas"].items():
            if checar_mes_contido:
                if entrada_data not in data:
                    continue
            
            if not checar_mes_contido:
                if not (converter_data(data) >= dt_inicial and converter_data(data) <= dt_final):
                    continue
           
            novo_dicionario.setdefault(data, {})[num] = qtd_horas
            total_horas += qtd_horas

    datas_ordenadas = dict(sorted(novo_dicionario.items(), key=lambda item: converter_data(item[0])))                
    return datas_ordenadas, total_horas


def data_especifica() -> None:
    while True:
        data = input("Digite uma data específica (ou 'q' para sair): ")
        if data == "q" or not data:
            return
            
        if (data := formatar_data(data)) == "formato invalido":
            continue
        
        #Ordenar por numero da demanda
        demandas_ordenadas = sorted(demandas.keys(), reverse=True)
        
        limpar_terminal()
        print(f"{azul}Data - {data}{reset}")
        print("-" * 30)
        
        total_horas = 0
        for num in demandas_ordenadas:
            horas_da_data = demandas[num]["datas"].get(data)
            if horas_da_data is None:
                continue
            total_horas += horas_da_data
            print(f"{amarelo}{num} - {demandas[num]["titulo"]}{reset}")
            print(f"{azul}Horas: {horas_da_data}h{reset}")
            print("-" * 30)
        
        print(f"{verde}Horas totais: {total_horas}h{reset}\n")
        input("Aperte 'enter' para voltar.")
        break
        
        
def mes_especifico() -> None: # Ordenar por mes
    while True:
        print("Digite mês (nome ou número) ou o mês e o ano (ou 'q' para sair)")
        data = input("> ")
        
        if data == "q" or not data:
            return
        
        data = mes_nome_para_numero(data)

        if (data := formatar_mes_e_ano(data)) == "formato invalido":
            continue

        datas_ordenadas, total_horas = criar_dict_datas(checar_mes_contido=True,
                                                        entrada_data=data)
            
        limpar_terminal()
        for data in datas_ordenadas:
            for numero_demanda in datas_ordenadas[data]:
                print(f"{amarelo}{numero_demanda} - {demandas[numero_demanda]["titulo"]}{reset}")
                print(f"{azul}{data}: {datas_ordenadas[data][numero_demanda]}h{reset}")
                print("-" * 30)

        print(f"{verde}Total horas: {total_horas}{reset}\n")
        input("Digite 'enter' para voltar")
        break


def periodo() -> None: # Ordernar por data
    while True:
        print("Digite um período (separe as datas por espaços) (ex: '01/01/23 01/01/24')")
        dados = input("> ").split()

        if not dados or dados[0] == "q":
            return
        
        data_inicial = dados[0] 
            
        if (data_inicial := formatar_data(data_inicial)) == "formato invalido":
            continue
        
        if len(dados) == 1:
            data_final = datetime.now().strftime("%d/%m/%Y")
        
        elif len(dados) == 2:
            if (data_final := formatar_data(dados[1])) == "formato invalido":
                continue
        else:
            print(f"{red}Formato inválido{reset}")
            continue
        
        datas_ordenadas, total_horas = criar_dict_datas(
                                        checar_mes_contido=False,
                                        dt_inicial=converter_data(data_inicial),
                                        dt_final=converter_data(data_final)
                                        )
        
        limpar_terminal()
        for datas in datas_ordenadas:
            for numero_demanda in datas_ordenadas[datas]:
                print(f"{amarelo}{numero_demanda} - {demandas[numero_demanda]["titulo"]}{reset}")
                print(f"{azul}{datas}: {datas_ordenadas[datas][numero_demanda]}h{reset}")
                print("-" * 30)
        
        print(f"{verde}Total horas: {total_horas}{reset}\n")
        input("Digite 'enter' para voltar")
        break            
        
        
def relatorios_apontamentos() -> None:
    while True:
        limpar_terminal()
        print("1. Data específica\n2. Mês específico\n3. Período\n4. Voltar (enter)")
        entrada = input("> ")
        match entrada:
            
            case "4"|"" | "q":
                return
            
            case "1":
                data_especifica()
            
            case "2":
                mes_especifico()
            
            case "3":
                periodo()
