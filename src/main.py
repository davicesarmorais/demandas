import random
from time import sleep
from lib.lib import *
from cadastro.cadastro import *
from pesquisar_demanda import pesquisar_demanda
from relatorios import relatorios_apontamentos
from editar_keybindings import *


def main():
    while True:
        limpar_terminal()
        print(f"{'{ Demandas }':-^80}")
        printar_numero_e_titulo(somente_ativas=True)
        print("-" * 80)
        
        print("\n[?] - Ajuda",
            "\n> ⌕ - Pesquisar demanda (digite o número da demanda)",
            f"\n> {keybind['editarDemanda']} - Editar/Cadastrar demanda",
            f"\n> {keybind['relatoriosApontamentos']} - Ver relatórios de apontamentos",
            f"\n> {keybind['listarAtivas']} - Listar demandas em execução",
            f"\n> {keybind['listarConcluidas']} - Listar demandas concluídas",
            f"\n> {keybind['editarAtalhos']} - Editar atalhos"
            f"\n> {keybind['fecharPrograma']} - Salvar e fechar programa",)
        
        entrada = input("> ").upper()
        
        if entrada in demandas:
            pesquisar_demanda(numero_demanda=entrada)
            continue
        
        
        if entrada == keybind["editarDemanda"]:
            add_remove_edit_demanda()
        
        
        elif entrada == keybind["relatoriosApontamentos"]:
            relatorios_apontamentos()    
        
        
        elif entrada == keybind["listarAtivas"]:
            limpar_terminal()
            printar_todas_demandas(status="ativa")
            input("Aperte 'enter' para voltar")
        
            
        elif entrada == keybind["listarConcluidas"]:
            limpar_terminal()
            printar_todas_demandas(status="concluida")
            input("Aperte 'enter' para voltar")


        elif entrada == keybind['editarAtalhos']:
            editar_keybinds()

        
        elif entrada == keybind["fecharPrograma"]: # Fechar programa
            limpar_terminal()
            print("Salvando...", end='\r')
            sleep(random.randint(4, 9)/10)
            print("Dados salvos.")
            sleep(random.randint(2, 6)/10)
            print("Fechando programa...")
            sleep(random.randint(2, 6)/10)
            break

    
        elif entrada == "?":
            limpar_terminal()
            print("Para obter ajuda confira o README no github com todas as funções explicadas.")
            print("\nhttps://github.com/davicesarmorais/demandas/blob/main/README.md\n")
            input("Aperte 'enter' para voltar.")

            
        else:
            print(f"{azul}Comando não encontrado{reset}")
            sleep(.5)
                
                          
if __name__ == "__main__":
    main()