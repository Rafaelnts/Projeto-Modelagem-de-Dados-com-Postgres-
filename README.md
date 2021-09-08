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
