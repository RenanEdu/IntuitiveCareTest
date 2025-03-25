import pdfplumber
import csv
import os
from zipfile import ZipFile

# 2.1 Extração de dados do PDF
pdf_path = "pdfs/Anexo-I.pdf"
csv_path = "Rol_de_Procedimentos.csv"

data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            data.extend(table)

# 2.2 Salvar os dados em um arquivo CSV 
with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print(f"Dados extraídos e salvos em: {csv_path}")

# 2.3 Compactar o CSV em um arquivo ZIP
zip_name = f"Teste_seu_nome.zip"
with ZipFile(zip_name, "w") as zipf:
    zipf.write(csv_path, arcname=os.path.basename(csv_path))

print(f"Arquivo CSV compactado em: {zip_name}")

# 2.4 Substituir abreviações (OD e AMB)
with open(csv_path, mode="r", encoding="utf-8") as csv_file:
    rows = list(csv.reader(csv_file))

# Substitui abreviações nas colunas
for row in rows:
    rows = [col.replace("OD", "Descrição OD").replace("AMB", "Descrição AMB") for col in row]

# Salvca o CSV atualizado
with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)

print(f"Abreviações substituídas no arquivo CSV: {csv_path}")

