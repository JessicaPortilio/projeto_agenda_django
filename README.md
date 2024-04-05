# Meu Projeto Django

Este é o meu projeto Django Agenda! Aqui estão as etapas para configurar o ambiente e executar o servidor localmente.

## Configuração do Ambiente Virtual

1. Primeiro, crie um ambiente virtual:
    ```
    python -m venv venv
    ```

2. Ative o ambiente virtual (no Windows):
    ```
    venv\Scripts\activate
    ```

## Instalação do Django

3. Instale o Django:
    ```
    pip install django
    ```

## Migração do Banco de Dados

4. Migre a base de dados do Django:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Coleta de Arquivos Estáticos

5. Colete arquivos estáticos:
    ```
    python manage.py collectstatic
    ```

## Instalação de Dependências Adicionais

6. Instale o Pillow:
    ```
    pip install Pillow
    ```

7. Instale o Faker:
    ```
    pip install faker
    ```

## Execução do Servidor

8. Finalmente, suba o servidor para verificar se está tudo funcionando:
    ```
    python manage.py runserver
    ```
Obs: Se quiser adicionar vários contatos aleatórios para teste pode rodar o código da pasta utils
