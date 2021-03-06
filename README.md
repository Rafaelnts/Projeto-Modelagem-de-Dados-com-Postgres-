# Projeto Modelagem de Dados com Postgres

## Introdução

Uma startup chamada Sparkify quer analisar os dados que eles vêm coletando em músicas e atividades do usuário em seu novo aplicativo de streaming de música.
A equipe de análise está particularmente interessada em entender quais músicas os usuários estão ouvindo. Atualmente, eles não têm uma maneira fácil de consultar seus
dados, que reside em um diretório de registros JSON sobre a atividade do usuário noaplicativo, bem como um diretório com metadados JSON nas músicas em seu aplicativo.

Eles gostariam que um engenheiro de dados criasse um banco de dados postgres com tabelas projetadas para otimizar consultas na análise de reprodução de músicas e trazêlo no projeto. Sua função é criar um esquema de banco de dados e um pipeline ETL para esta análise. Você poderá testar seu banco de dados e pipeline ETL executando
consultas dadas a você pela equipe de análise da Sparkify e comparar seus resultados com os resultados esperados.

## Descrição do projeto

Para concluir o projeto, você precisará definir tabelas de fatos e dimensões para um esquema estelar para um determinado foco analítico e escrever um pipeline ETL que
transfere dados de arquivos em dois diretórios locais para essas tabelas em Postgres usando Python e SQL.

## Conjunto de dados de música

O primeiro conjunto de dados é um subconjunto de dados reais do Million Song Dataset.
Cada arquivo está no formato JSON e contém metadados sobre uma música e o artista dessa canção. Os arquivos são particionados pelas três primeiras letras do ID da faixa de
cada canção. Por exemplo, aqui estão os filepaths para dois arquivos neste conjunto de dados.
## Song_data
>`song_data/A/B/C/TRABCEI128F424C983.json`

>`song_data/A/A/B/TRAABJL12903CDCF1A.json`

E abaixo está um exemplo de como é um único arquivo de música, **TRAABJL12903CDCF1A.json.**

>` {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null,
"artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud",
"song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036,"year": 0}`


## Log Data

>`The second dataset consists of log files in JSON format generated by this [event
simulator](https://github.com/Interana/eventsim) based on the songs in the dataset
above. These simulate activity logs from a music streaming app based on specified
configurations.
The log files in the dataset you'll be working with are partitioned by year and month.
For example, here are filepaths to two files in this dataset.`

**log_data/2018/11/2018-11-12-events.json**

**log_data/2018/11/2018-11-13-events.json**

Se você quiser olhar para os dados **JSON** dentro de **log_data** arquivos, você precisará
criar um dataframe pandas para ler os dados. Lembre-se de primeiro importar bibliotecas
**JSON** e **pandas**.

>df = pd.read_json(filepath, lines=True)
>
Por exemplo, leria o arquivo de dados 
>2018-11-01-events.json. df =
pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True)

Caso você precise de uma atualização nos formatos de arquivo JSON

## Esquema para análise de reprodução de música

Usando os conjuntos de dados de música e log, você precisará criar um esquema estelar
otimizado para consultas na análise de reprodução de músicas. Isso inclui as seguintes
tabelas.

**Diagrama do esquema do banco de dados**  

![image](https://raw.githubusercontent.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/main/Diagrama.png)


**Tabela de Fatos**

1. **songplays** - registros em dados de registro associados a reproduções de músicas,
ou seja, registros com página NextSong o songplay_id, start_time, user_id, nível, song_id, artist_id, session_id,
localização, user_agent

**Tabelas de dimensão**

2. **usuários** - usuários no aplicativo
o user_id, first_name, last_name, gênero, nível

3. **músicas** - músicas no banco de dados de música
o song_id, título, artist_id, ano, duração

4. **artistas** - artistas em banco de dados de música
o artist_id, nome, localização, latitude, longitude

5. **tempo** - timestamps de discos em songplays divididos em unidades específicas
o start_time, hora, dia, semana, mês, ano, dia da semana

## Bibliotecas necessárias

- `pandas`
- `psycopg2`
- `sql_queries`

## Motivação

Aprendo Modelagem de Dados com RDM usando metadados JSON que representam as músicas e arquivos JSON que representam a atividade do usuário.

### :pushpin: Etapas do Projeto

Abaixo estão as etapas que você pode seguir para concluir o projeto:

Criar tabelas

1. Escreva declarações para criar cada tabela. CREATE [create_tables.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/create_tables.py)
2. Escreva declarações para derrubar cada tabela se ela existir. DROP [sql_queries.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/sql_queries.py)
3. Criar seu banco de dados e tabelas. [create_tables.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/create_tables.py)
4. Para confirmar a criação de suas tabelas com as colunas corretas. Certifique-se de
clicar em "Reiniciar o kernel" para fechar a conexão ao banco de dados depois de executar este notebook. [test.ipynb](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/test.ipynb)

### Para criar todas as tabelas de que precisava, executei as quatro etapas a seguir:

*Escreva as instruções CREATE em [sql_queries.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/sql_queries.py) para criar cada tabela de acordo com o esquema definido acima.*

*Escreva instruções DROP em [sql_queries.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/sql_queries.py) para eliminar cada tabela, se houver.*

*Execute [create_tables.py](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/create_tables.py) para criar o banco de dados e as tabelas.*

*Execute [test.ipynb](https://github.com/Rafaelnts/Projeto-Modelagem-de-Dados-com-Postgres-/blob/main/test.ipynb)
 para confirmar a criação das tabelas com as colunas corretas.* 
 
 *Certifique-se de clicar em "Reiniciar kernel" para fechar a conexão com o banco de dados após executar este notebook.*
