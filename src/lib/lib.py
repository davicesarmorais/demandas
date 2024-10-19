import json, os
from lib.cores import *
from datetime import datetime


def limpar_terminal() -> None:
    os.system("cls||clear")


def abrir_arquivo() -> None:
    try:
        with open("demandas.json", "r") as file:
            demandas = json.load(file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("demandas.json", "w") as file:
            demandas = {}
            json.dump(demandas, file)

    return demandas


demandas = abrir_arquivo()


def salvar_no_json(arquivo : str, dicionario: dict) -> None:
    with open(arquivo, "w") as file:
        json.dump(dicionario, file, indent=4)

def printar_uma_demanda(numero_demanda: str, com_horas: bool) -> None:
    demanda = demandas[numero_demanda]
    cor_status = azul if demanda["status"] == "ativa" else verde
    
    print(f"{amarelo}{numero_demanda} - {demanda["titulo"]}{reset}")    
    print(f"Estimativa: {roxo}{demanda["estimativa"]}{reset}")    
    print(f"Status: {cor_status}{demanda["status"]}{reset}")
    
    horas_gastas = sum(demanda["datas"].values())
    horas_restantes = demanda["estimativa"] - horas_gastas
    print(f"Horas gastas: {verde}{horas_gastas}{reset}")
    print(f"Horas restantes: {red}{horas_restantes}{reset}\n")
    
    if com_horas:
        for data in demanda["datas"]:
            print(f"{data}: {demanda["datas"][data]}")
        if demanda["datas"]:
            print()


def printar_todas_demandas(status: str) -> None:
    cor_status = azul if status == "ativa" else verde
    
    horas_totais = 0
    for num in demandas:
        demanda = demandas[num]
        if demanda["status"] == status:
            print(f"{amarelo}{num} - {demanda["titulo"]}{reset}")    
            print(f"Estimativa: {roxo}{demanda["estimativa"]}{reset}")    
            print(f"Status: {cor_status}{demanda["status"]}{reset}")
            
            horas_gastas = sum(demanda["datas"].values())
            horas_restantes = demanda["estimativa"] - horas_gastas
            print(f"Horas gastas: {verde}{horas_gastas}h{reset}")
            print(f"Horas restantes: {red}{horas_restantes}h{reset}\n")
            horas_totais += horas_gastas
    print(f"{verde}Horas totais: {horas_totais}h{reset}\n")


def printar_numero_e_titulo(somente_ativas: bool = False) -> None:
    if not demandas:
        print("Nenhuma demanda registrada.")
        return
    
    for num in demandas:
        if somente_ativas:
            if demandas[num]["status"] == "ativa":
                print(f"{num} - {demandas[num]["titulo"]}")
        else:
            print(f"{num} - {demandas[num]["titulo"]}")


def formatar_data(entrada_data: str) -> str:
    formatos_aceitos = ["%d", "%d/%m", "%d-%m", "%d%m" ,"%d/%m/%y", "%d/%m/%Y", "%d%m%y", "%d%m%Y", "%d-%m-%y", "%d-%m-%Y"]
    mes_atual = datetime.now().strftime("%m")
    ano_atual = datetime.now().strftime("%Y")
    
    for idx, formato in enumerate(formatos_aceitos):
        try:
            data = datetime.strptime(entrada_data, formato)
        except ValueError:
            continue
              
        if idx == 0:
            data = datetime.strftime(data, f"%d/{mes_atual}/{ano_atual}")
        elif idx in range(1,4):
            data = datetime.strftime(data, f"%d/%m/{ano_atual}")
        else:
            data = data.strftime("%d/%m/%Y")    
    
        if datetime.strptime(data, "%d/%m/%Y") > datetime.now():
            print(f"{red}Não é possível inserir uma data futura{reset}")
            return "formato invalido"
        
        return data
    
    else:
        print(f"{red}Formato inválido{reset}")
        return "formato invalido"
    