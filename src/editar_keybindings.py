import json
from time import sleep
from lib.lib import salvar_no_json, limpar_terminal
from lib.cores import *


try:
    with open("keybindings.json", 'r') as file:
        keybind = json.load(file)
except FileNotFoundError:
    with open("keybindings.json", 'w') as file:
        keybind = {
            "editarDemanda": "Q",
            "relatoriosApontamentos": "W",
            "listarAtivas": "E",
            "listarConcluidas": "A",
            "editarAtalhos": "S",
            "fecharPrograma": "D"
        }
        json.dump(keybind, file, indent=4)


def printar_opcoes(opcoes):
    for chave, valor in opcoes.items():
        print(f"{chave} - {valor[1]}")

    
def editar_keybinds():
    while True:
        opcoes = {keybind['editarDemanda']: ['editarDemanda', 'Editar/Cadastrar demanda'],
                    keybind['relatoriosApontamentos']: ['relatoriosApontamentos', 'Ver relatórios de apontamentos'],
                    keybind['listarAtivas']: ['listarAtivas', 'Listar demandas em execução'],
                    keybind['listarConcluidas']: ['listarConcluidas', 'Listar demandas concluídas'],
                    keybind['editarAtalhos']: ['editarAtalhos', 'Editar atalhos'],
                    keybind['fecharPrograma']: ['fecharPrograma', 'Salvar e fechar programa']}
        
        limpar_terminal()
        printar_opcoes(opcoes)
        print("\nDigite o atalho que deseja editar (digite 'sair' ou aperte 'enter' para fechar)")
        atalho_escolhido = input("> ").upper()
        
        if atalho_escolhido == "SAIR" or not atalho_escolhido:
            return
        
        if atalho_escolhido not in opcoes:
            print(f"{red}Opção não encontrada.{reset}")
            sleep(.5)
            continue
            
        while True:
            limpar_terminal()
            printar_opcoes(opcoes)
            print("\nPara voltar digite 'voltar' ou aperte 'enter'")
            print(f"Opcão selecionada: [{atalho_escolhido}] -> Digite o novo atalho")
            novo_atalho = input("> ").upper()
            
            if novo_atalho == "SAIR" or not novo_atalho:
                break
            
            if len(novo_atalho) > 1:
                print(f"{red}Digite apenas 1 caractere{reset}")
                sleep(.5)
                continue 
            
            if novo_atalho.isdecimal():
                print(f"{red}Números não são permitidos (conflitam com os números das demandas){reset}")
                sleep(1)
                continue

            if novo_atalho in keybind.values():
                limpar_terminal()
                printar_opcoes(opcoes)
                print(f"{azul}\nAtalho já registrado em '{opcoes[novo_atalho][1]}'{reset}")
                print("Deseja confirmar a permuta do atalho? (s/n)")
                confirmar = input("> ")
                
                if confirmar == "s":
                    chave_atalho_escolhido = opcoes[atalho_escolhido][0]
                    chave_atalho_ja_registrado = opcoes[novo_atalho][0]
                    
                    keybind[chave_atalho_escolhido] = novo_atalho
                    keybind[chave_atalho_ja_registrado] = atalho_escolhido
                    
                else:
                    print(f"{azul}Operação cancelada{reset}")
                    sleep(0.5)
                    continue    
            
            
            if novo_atalho not in keybind.values():        
                atalho_escolhido = opcoes[atalho_escolhido][0]
                keybind[atalho_escolhido] = novo_atalho

            
            salvar_no_json(arquivo='keybindings.json', dicionario=keybind)
            print(f"{verde}Atalho atualizado com sucesso!{reset}")
            sleep(1)
            break
        