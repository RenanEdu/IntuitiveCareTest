import os

# Executa o Web Scraping
os.system("python scraping_service/web_scraping.py")

# Baixa os dados das operadoras ativas
os.system("python database_service/operadoras_ativas/download_operadoras.py")

# Transforma os dados do PDF em CSV
os.system("python transform_service/transform_service.py")