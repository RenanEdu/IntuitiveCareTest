import os
import requests
from bs4 import BeautifulSoup

# Função para baixar arquivos de um repositório
def download_files(base_url, output_dir, file_extension=".zip"):
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a', href=True):
        file_name = link['href']
        if file_name.endswith(file_extension):
            file_url = base_url + file_name
            print(f"Baixando: {file_url}")
            file_response = requests.get(file_url)
            file_response.raise_for_status()
            with open(os.path.join(output_dir, file_name), "wb") as file:
                file.write(file_response.content)
            print(f"Salvo em: {os.path.join(output_dir, file_name)}")

# URLs dos Repositórios
demonstracoes_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"

# Diretórios de saída
demonstracoes_dir = "database_service/demonstracoes_contabeis"
operadoras_dir = "database_service/operadoras_ativas"

# Baixa arquivos das demonstrações contábeis (últimos dois anos)
download_files(demonstracoes_url, demonstracoes_dir, file_extensio=".zip")

# Baixa os arquivos das operadoras ativas
download_files(operadoras_url, operadoras_dir, file_extensio=".csv")