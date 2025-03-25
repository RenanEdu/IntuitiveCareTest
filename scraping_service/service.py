import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# 1.1 Acessar o site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
response.raise_for_status()

# Parsear o HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 1.2 Encontrar e baixare os PDFs (Anexo I e II)
pdf_links= []
for link in soup.find_all('a', href=True):
    if "Anexo-I" in link['href'] or "Anexo-II" in link[href]:
        pdf_links.append(link['href'])

# Criar pasta para salvar os PDFs
os.makedirs('pdfs', exist_ok=True)

# Baixar os PDFs
for pdf_url in pdf_links:
    pdf_response = requests.get(pdf_url)
    pdf_response.raise_for_status()
    pdf_name = os.path.join("downloads", pdf_url.split("/")[-1])
    with open(pdf_name, "wb") as pdf_file:
        pdf_file.write(pdf_response.content)
    print(f"Baixado: {pdf_name}")

# 1.3 Compactar os PDFs em um único arquivo ZIP
zip_name = "anexos.zip"
with ZipFile(zip_name,'w') as zipf:
    for root, _, files in os.walk("downloads"):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)
print(f"Arquivos compactados em: {zip_name}")