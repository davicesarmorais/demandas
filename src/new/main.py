from lib.lib import *
from time import sleep
from cadastro.cadastro import *
from pesquisar_demanda import pesquisar_demanda
from relatorios import relatorios_apontamentos
import random


def main():
    while True:
        limpar_terminal()
        print(f"{'{ Demandas }':-^80}")
        printar_numero_e_titulo(somente_ativas=True)
        print("-" * 80)
        
        print("\n[?] - Ajuda",
            "\n> ⌕ - Pesquisar demanda (digite o número da demanda)",
            "\n> Q - Editar/Cadastrar demanda",
            "\n> W - Ver relatórios de apontamentos",
            "\n> A - Listar demandas em execução",
            "\n> S - Listar demandas concluídas",
            "\n> D - Salvar e fechar programa",)
        
        entrada = input("> ")
        
        if entrada in demandas:
            pesquisar_demanda(numero_demanda=entrada)
            continue
        
        match entrada.lower():
            case "q":
                cadastrar_demanda()
            
            case "w":
                relatorios_apontamentos()    
            
            case "a":
                limpar_terminal()
                printar_todas_demandas(status="ativa")
                input("Aperte 'enter' para voltar")
                
            case "s":
                limpar_terminal()
                printar_todas_demandas(status="concluida")
                input("Aperte 'enter' para voltar")

            case "d": # Fechar programa
                limpar_terminal()
                print("Salvando...", end='\r')
                sleep(random.randint(4, 9)/10)
                print("Dados salvos.")
                sleep(random.randint(2, 6)/10)
                print("Fechando programa...")
                sleep(random.randint(2, 6)/10)
                break
        
            case "?":
                limpar_terminal()
                print("Para obter ajuda confira o README no github com todas as funções explicadas.")
                print("\nhttps://github.com/davicesarmorais/demandas/blob/main/README.md\n")
                input("Aperte 'enter' para voltar.")
                
                
                
if __name__ == "__main__":
    main()