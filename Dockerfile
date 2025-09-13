# 1. Imagem base oficial do Python
FROM python:3.11-slim

# 2. Define diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia requirements primeiro (melhora cache do Docker)
COPY requirements.txt .

# 4. Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do código
COPY . .

# 6. Expõe a porta usada pelo FastAPI
EXPOSE 8000

# 7. Comando para rodar o servidor FastAPI com uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
