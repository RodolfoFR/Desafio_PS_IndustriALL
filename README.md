# Desafio_PS_IndustriALL
Esse Repositório é referente ao desafio do processo seletivo da IndustriALL

**Dono do Repositótio:** Rodolfo Franco Ribeiro

# Desafio:

Contratado por uma Startup especialista no desenvolvimento de soluções de
Inteligência Artificial para os mais diversos setores industriais. Papel é criar um modelo
preditivo utilizando dados dos sensores da planta para identificar padrões que precedem falhas
no equipamento.


# Objetivo:

O objetivo é criar um modelo preditivo que possa identificar antecipadamente as possíveis falhas de um equipamento em específico a partir dos valores dos demais sensores da planta. explorar, analisar e modelar os dados dos sensores para prever possíveis falhas no equipamento industrial. Isso envolve a preparação dos dados, identificação de padrões ou comportamentos anômalos que possam indicar falhas iminentes e a criação de um modelo preditivo capaz de prever essas falhas com uma boa precisão. 

# Dados Bruto do Desafio:

Os dados bruto do desafio consiste em uma pasta com 53 arquivo csv. Cada arquivo csv tem duas colunas: Uma coluna comum em todos os arquivo coluna "timestamp" referente a um minuto de medição dos sensores da planta, que começa do primeiro minuto do dia 01/04/2018 a ultimo minuto 31/08/2018. E outra coluna varia de arquivo a arquivo. Analisando os arquivos foi possível inferir que os arquivos  TAG_iALL_PS_00.csv, TAG_iALL_PS_01.csv, TAG_iALL_PS_02.csv, ..., TAG_iALL_PS_51.csv são as medições de algum sensor, ou seja, a entrada. E o arquivo target_iALL_PS.csv apresenta na sua coluna individual o estado da planta industrial: Normal ou Anormal, ou seja, a saída.

# Metodologia

Como os dados são com base no tempo vai ser criado um modelo RNN (Rede Neural Recorrente), a hipótese é que os tempos anteriores a um dado instante podem influênciar o estado da planta naquele instante. Para isso realizar um pré-processamento nos dados para atender ao modelo predetivo. 

# Códigos:

  - Importante
      + Para mexer nos código é preciso mexer no caminho da variavel path_of_PS_IndustriALL (str) presente em todos os códigos. É o caminho do diretório que foi colcado a respositório
  
  - Bibliotecas
    + sys, os, pandas, matplotlib, numpy

  - Ambiente usado para o projeto
    + Google Colab

  - data_preprocessing.ipynb:
    + Objetivo: Realizar o tratamento dos dados
    + 1°: Carregar os arquivos csv dos Dados Brutos
    + 2°: Montar um único DataFrame/Tabela com esses Dados, sem repetir a coluna comum "timestamp", onde cada arquivo teria uma coluna no Dataframe/Tabela
        * Total de linhas/dados de 220320
        * Total de Coulnas: 54
    + 3°: Verificar se há arquivos com colunas iguais ou colunas com linhas vazias
        * Foi Removido TAG_iALL_PS_15, pois está com linhas vazias
        * Total de Coulnas: 53
    + 4° Verificação se há linhas duplicadas
    + 5° Remoção de linhas com pelo menos uma coluna/entrada vazias
        * 101217 dados/linhas removidos, sobrando 119103 dados
    + 6° Análise das saídas:
        * Duas classes: Normal (0) e Anormal (1)
        * 97,5% dos dados totais são da classe Normal e 2,5% são Anormal
        * Evidente um desbalanceamento dos dado    
    + 7° Análise das médias, desvio padrão, coeficiente de variação e dos histogramas de cada tipo de entrada/coluna
    + 8° Critérios para remover algumas colunas:
        * Coeficiente de variação (cv) abaixo da média dos coeficientes de variação menos o desvio padrão das entradas (menor que 27.4%)
        * Colunas que tem seus histogramas de classe (um histograma por classe - Normal e Anormal) com a área de intersecção maior ou igual a 75%
        * Entradas com esses critério tem baixa variação no tempo e pouco influência a saída
        * Colunas/Entradas Removidas:  













