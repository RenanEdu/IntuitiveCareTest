# Testes de Nivelamento

Este repositório contém a implementação dos testes de nivelamento, incluindo tarefas de Web Scraping, Transformação de Dados, Banco de Dados e API.

## Estrutura do Projeto

- **1. Teste de Web Scraping**: Código para acessar o site da ANS, baixar os anexos I e II em formato PDF e compactá-los em um único arquivo ZIP.
- **2. Teste de Transformação de Dados**: Extração de dados de um PDF, transformação em CSV e compactação.
- **3. Teste de Banco de Dados**: Scripts SQL para criação de tabelas, importação de dados e consultas analíticas.
- **4. Teste de API**: Interface web em Vue.js e servidor Python para busca textual em dados de operadoras.

---

## Requisitos


### Dependências 
- Python 3.7 ou superior
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`

### Instalação das Dependências
Execute o comando abaixo para instalar as dependências necessárias:

```bash
pip install requests beautifulsoup4