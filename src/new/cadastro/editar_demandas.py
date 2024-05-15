from lib.lib import *
from lib.cores import *
from time import sleep


def get_numero_demanda(checar_presenca: bool = True) -> str:
    while True:
        numero_demanda = input("Digite o NÚMERO da demanda: ")

        if numero_demanda == 'q' or not numero_demanda:
            return 'sair'

        if checar_presenca and numero_demanda in demandas:
            print(f"{red}Número já registrado.{reset}")
            continue
        
        if checar_presenca and not numero_demanda.isdecimal():
            print(f"{red}Digite um número{reset}")
            continue
        
        if not checar_presenca and numero_demanda not in demandas:
            print(f"{red}Demanda não encontrada.{reset}")
            continue

        return numero_demanda


def get_informacao(opcoes: dict) -> str:
    print("Digite o número da demanda que quer editar (ou 'q' para voltar).")
    while True:
        informacao = input("> ")
        
        if informacao == "q" or not informacao:
            return 'sair'
        
        if informacao not in opcoes:
            print(f"{red}Opção não encontrada{reset}")
            continue
            
        return opcoes.get(informacao)


def get_nova_informacao(informacao, numero_demanda) -> str:
    limpar_terminal()
    printar_uma_demanda(numero_demanda, com_horas=True)
    print(f"Digite qual o novo valor para o/a {informacao} (ou 'q' para cancelar).")
    while True:
        nova_informacao = input("> ")
        
        if nova_informacao == "q" or not nova_informacao:
            return 'cancelar'
        
        if informacao == "estimativa" or informacao == "numero" and not nova_informacao.isdecimal():
            print(f"{red}Digite um número{reset}")
            continue
        
        if informacao == "numero" and nova_informacao in demandas:
            print(f"{red}Esse número já está registrado{reset}")
            continue
        
        if informacao == "estimativa":
            return int(nova_informacao)
        else:
            return nova_informacao
    
    
def editar_informacao(informacao, nova_informacao, numero_demanda) -> None:
    if informacao == "numero":
        copia = {nova_informacao: demandas[numero_demanda]}
        del demandas[numero_demanda]
        demandas.update(copia)
    
    else:
        demandas[numero_demanda][informacao] = nova_informacao
    
    
def confirmar_edicao(informacao, nova_informacao, numero_demanda) -> None:
    print(f"{azul}Você deseja editar o/a {informacao} para {nova_informacao}? (s/n){reset}")
    confirmacao = input("> ")

    if confirmacao == "s":
        editar_informacao(informacao, nova_informacao, numero_demanda)
        print(f"{verde}Demanda {numero_demanda} editada com sucesso{reset}")
        salvar_no_json()
        sleep(1)        
    else:
        print(f"{azul}Operação cancelada{reset}")
        sleep(0.5)
        limpar_terminal()
        
    if informacao == "numero":
        return "numero"
    
    
def mudar_data(numero_demanda, data_antes) -> str | None:
    while True:
        print("Digite a nova data. (ou 'q' para voltar)")
        nova_data = input("> ")
        
        if nova_data == "q" or not nova_data:
            limpar_terminal()
            return
        
        if nova_data in demandas[numero_demanda]["datas"]:
            print(f"{red}Data já registrada.{reset}")
            continue
        
        if (nova_data := formatar_data(entrada_data=nova_data)) == "formato invalido":
            continue
                
        print(f"{azul}Você tem certeza que quer alterar a data para {nova_data}? (s/n){reset}")
        confirmacao = input("> ")
        
        if confirmacao == "s":
            copia = demandas[numero_demanda]["datas"][data_antes]
            del demandas[numero_demanda]["datas"][data_antes]
            demandas[numero_demanda]["datas"][nova_data] = copia
            salvar_no_json()
            print(f"{verde}Demanda atualizada com sucesso!{reset}")
            sleep(1)
            return "fechar"
        else:
            print(f"{azul}Operação cancelada.{reset}")
            sleep(.5)
            limpar_terminal()
        
        
def mudar_horas(numero_demanda, data_antes) -> str | None:
    while True:
        print("Digite a nova hora (ou 'q' para voltar)")
        nova_hora = input("> ")
        
        if nova_hora == "q" or not nova_hora:
            limpar_terminal()
            return
        
        if not nova_hora.isdecimal():
            print(f"{red}Digite um número{reset}")
            continue
        
        print(f"{azul}Você tem certeza que quer alterar as horas para {nova_hora}? (s/n){reset}")
        confirmacao = input("> ")
        
        if confirmacao == "s":
            demandas[numero_demanda]["datas"][data_antes] = int(nova_hora)
            salvar_no_json()
            print(f"{verde}Demanda atualizada com sucesso!{reset}")
            sleep(1)
            return "fechar"
        else:
            print(f"{azul}Operação cancelada.{reset}")
            sleep(.5)
            limpar_terminal()
            


def excluir_data(numero_demanda, data_antes) -> None:
    print(f"{azul}Você tem certeza que deseja {red}excluir {azul}essa data? (s/n){reset}")
    confirmacao = input("> ")
    
    if confirmacao == "s":
        del demandas[numero_demanda]["datas"][data_antes]
        salvar_no_json()
        print(f"{verde}Demanda atualizada com sucesso!{reset}")
        sleep(1)
        return "fechar"
    else:
        print(f"{azul}Operação cancelada.{reset}")
        sleep(.5)
        limpar_terminal()
        


def opcao_data(numero_demanda: str) -> None:
    while True:
        limpar_terminal()
        printar_uma_demanda(com_horas=True, numero_demanda=numero_demanda)
        print("Digite a data que quer editar (ou 'q' para cancelar): ")
        data_antes = input("> ")
        
        if data_antes == "q" or not data_antes:
            return
        
        data_antes = formatar_data(data_antes)
        
        if data_antes not in demandas[numero_demanda]["datas"]:
            print(f"{red}Data não encontrada.{reset}")
            sleep(.5)
            continue
        
        while True:
            limpar_terminal()
            printar_uma_demanda(com_horas=False, numero_demanda=numero_demanda)
            print(f"{data_antes}: {demandas[numero_demanda]["datas"][data_antes]}\n")
                    
            print("1. Mudar data\n2. Mudar horas\n3. Exluir data\n4. Voltar (enter)")
            
            entrada = input("> ")
            match entrada:
                case "4" | "" : # Voltar
                    break
                
                case "1": 
                    if mudar_data(numero_demanda, data_antes) == "fechar":
                        break
                        
                case "2": 
                    if mudar_horas(numero_demanda, data_antes) == "fechar":
                        break
                        
                case "3": 
                    if excluir_data(numero_demanda, data_antes) == "fechar":
                        break
    
    
def opcao_status(numero_demanda) -> str | None:
    limpar_terminal()
    printar_uma_demanda(numero_demanda, com_horas=True)
    estado = demandas[numero_demanda]["status"]
    cor_estado_antes = azul if estado == "ativa" else verde
    cor_estado_depois = verde if estado == "ativa" else azul
    
    print(f"O atual estado da demanda é: {cor_estado_antes}{estado}{reset}")
    novo_estado = "concluida" if estado == "ativa" else "ativa"
    
    print(f"Você deseja alterar o estado para {cor_estado_depois}{novo_estado}{reset}? (s/n)")
    confirmacao = input("> ")
    
    if confirmacao == "s":
        demandas[numero_demanda]["status"] = novo_estado
        salvar_no_json()
        print(f"{verde}Demanda atualizada com sucesso{reset}")
        sleep(1)
    else:
        print(f"{azul}Operação cancelada{reset}")
        sleep(0.5)
    
    
# Funcão principal
def editar_demandas() -> None:
    while True:
        limpar_terminal()
        print(f"{'{ Demandas }':-^80}")
        printar_numero_e_titulo()
        print("-" * 80)
        
        print("Para sair digite 'q'")
        # Pegar numero da demanda
        if (numero_demanda := get_numero_demanda(False)) == "sair":
            return
        
        # ----------------------------------------------
        
        while True:
            limpar_terminal()
            printar_uma_demanda(numero_demanda, com_horas=True)
            opcoes = {'n':'numero', 't':'titulo', 'e':'estimativa', 's':'status', 'h':'horas', 'd':'data'}
    
            print(f"Opções: [n]umero, [t]itulo, [e]stimativa, [s]tatus, [h]oras, [d]ata")
            
            # Pegar a informacao que quer editar
            if (informacao := get_informacao(opcoes)) == "sair":
                break
            
            # Alterar informacao de data
            if informacao in ["data", "horas"] :
                opcao_data(numero_demanda)
                continue

                     
            # Alterar informacao de status
            if informacao == "status":
                opcao_status(numero_demanda)
                continue
            
            # Alterar as outras informacoes
            if informacao not in ["data", "horas", "status"]:
                if (nova_informacao := get_nova_informacao(informacao, numero_demanda)) == "cancelar":
                    limpar_terminal()
                    continue
                
                if confirmar_edicao(informacao, nova_informacao, numero_demanda) == "numero":
                    break
                           
                        
                        