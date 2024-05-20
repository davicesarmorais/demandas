# Projeto demandas.

## O que é?

  - É um sistema feito para **armazenar e manipular demandas**.
  - É possível _cadastrar demandas_, _editar_, _remover_, _inputar horas_, _ver demandas em execução ou concluidas_, entre outras coisas.

  - Página principal <br>![Pagina inicial](/imgs/PaginaPrincipal.png)
  - Dentro de 'Pesquisar demandas'<br>![Input Horas](/imgs/InputHoras.png)
  - Dentro de 'Cadastrar/Editar demanda'<br>![Crud Demandas](/imgs/CRUDdemandas.png)

## Como funciona?

  1. **O usuário cadastra uma demanda.**
      - Contendo número da demanda;
      - Título da demanda;
      - Estimativa de horas.
  2. **Pode pesquisar essa demanda.**
      - É **exibida** essa demanda:
            <br>![EstruturaDemanda](/imgs/VerDetalhes.png)
      - É possível **inputar as horas** para essa demanda;
          - *Define-se uma data.*
          <br>![Data](/imgs/DeifinirData.png)
      
  3. **Pode editar uma demanda** 
      - No menu '*Cadastrar/Editar demandas*', na opção **3. Editar demanda**, você escolher essas opções:
        - **numero** -> Edita o número da demanda;
        - **titulo** -> Edita o título da demanda;
        - **estimativa** -> Edita a estimativa de horas da demanda;
        - **data/datas** -> Edita alguma data da demanda;
            - É possível tanto editar quanto excluir uma data.
        - **hora/horas** -> Edita as horas gastas de alguma data.
  4. **Pode visualizar o relatório de apontamentos.**
      - Há como pesquisar por *data específica*, *mês* ou *período*.
          - Data específica <br> ![Data especifica](/imgs/DemandasDiaEspecifico.png)
          - Mês e de um ano específico <br> ![Mes](/imgs/DemandaMesEspecifico.png)
          - Período <br> ![Periodo](/imgs/DemandaPeriodo.png)
  5. **Pode listar as demandas em execução ou concluídas.**
        - Demandas em execução <br> ![execucao](/imgs/DemandasAtivas.png)
        - Demandas concluídas <br> ![concluidas](/imgs/DemandasConcluidas.png)

# Ajuda / Dicas

## Manejo do software.
  
  - Para **selecionar** uma categoria, basta digitar alguma opção (*seja um número, ou uma confirmação como s/n*) e apertar enter.
  - Para **cancelar uma ação** ou **retroceder**, basta deixar um espaço em branco e apertar *'enter'*, *certifique-se de que não há nenhum caractere no terminal*.
  - Ao **inputar as horas**, o software verifica se há alguma hora inputada na data escolhida e **soma automaticamente**. Não é necessário se preocupar com isso.
  - 
## Dicas
  - **Leia sempre qual a informação o programa pede**, como formato de alguma data.
  - Coloque o **dado apropriado** para determinada condição.
      - Ex: Ao cadastrar uma demandas, coloque um número na estimativa das horas.
  - Tente **não fechar o software** enquanto ele processa alguma informação, apesar de ser bem seguro, é bom ter cuidado.
  - **Evite editar o _json_** para não comprometer o funcionamente do software
  - Caso o _json_ seja **apagado** ou não existir o arquivo, _o software cria um novo arquivo automaticamente_, não precisa criar manualmente :)
