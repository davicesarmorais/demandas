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
            <br>![EstruturaDemanda](/imgs/EstruturaDemanda.png)
      - É possível **inputar as horas** para essa demanda;
          - *Define-se uma data.*
          <br>![Data](/imgs/DeifinirData.png)
      - É possível **ver mais detalhes** dessa demanda;
          - Exibe a demanda (*número, título, estimativa, status, horas gastas e restantes*)
          - Exibe também as **datas com as horas gastas nelas**.
          <br>![Detalhes](/imgs/VerDetalhes.png)
  3. **Pode visualizar o relatório de apontamentos.**
      - Há como pesquisar por *data específica*, *mês* ou *período*.
          - Data específica <br> ![Data especifica](/imgs/DemandasDiaEspecifico.png)
          - Mês e de um ano específico <br> ![Mes](/imgs/DemandaMesEspecifico.png)
          - Período <br> ![Periodo](/imgs/DemandaPeriodo.png)
  4. **Pode listar as demandas em execução ou concluídas.**
        - Demandas em execução <br> ![execucao](/imgs/DemandasAtivas.png)
        - Demandas concluídas <br> ![concluidas](/imgs/DemandasConcluidas.png)

# Ajuda / Dicas

## Manejo do software.
  
  - Para **selecionar** uma categoria, basta digitar alguma opção (*seja um número, ou uma confirmação como s/n*) e apertar enter.
  - Para **cancelar uma ação** ou **retroceder**, é possível apertar *'enter'*, *certifique-se de que não há nenhum caractere no terminal*.
  - Ao **inputar as horas**, o software verifica se há alguma hora inputada na data escolhida e **soma automaticamente**. Não é necessário se preocupar com isso.
  - No menu '*Cadastrar/Editar demandas*', na opção **3. editar demandas**, há essas opções para escolher: **(Todas as opções podem ser escritas tanto em maiúculo quanto em minúsculo e com ou sem acento)**
      - **Número** -> Edita o número da demanda;
      - **Título** -> Edita o título da demanda;
      - **Estimativa** -> Edita a estimativa de horas da demanda;
      - **Data/datas** -> Edita alguma data da demanda;
          - É possível tanto editar quanto excluir uma data.
      - **Hora/horas** -> Edita as horas gastas de alguma data.
## Dicas
  - **Leia sempre qual a informação o programa pede**, como formato de alguma data.
  - Coloque o **dado apropriado** para determinada condição.
      - Ex: Ao cadastrar uma demandas, coloque um número na estimativa das horas.
  - Tente **não fechar o software** enquanto ele processa alguma informação, apesar de ser bem seguro, é bom ter cuidado.
  - **Evite editar o _json_** para não comprometer o funcionamente do software
  - Caso o _json_ seja **apagado** ou não existir o arquivo, _o software cria um novo arquivo automaticamente_, não precisa criar manualmente. :)
