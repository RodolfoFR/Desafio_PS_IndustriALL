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
