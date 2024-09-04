# syntax=docker/dockerfile:1.4

# Stage 1: Build environment (builder)
FROM --platform=$BUILDPLATFORM python:latest AS builder

WORKDIR /app

# Copia o código da aplicação
COPY . /app

# Copia e instala as dependências
COPY requirements.txt .

# Instala dependências de produção
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements-docker.txt

# Stage 2: Production environment (lean and optimized for distribution)
FROM python:latest AS production
WORKDIR /app

# Copia os arquivos do estágio de builder
COPY --from=builder /app /app

#ENV FLASK_ENV=production

# Expõe a porta 8000 para o contêiner
EXPOSE 8000

CMD ["python", "app.py"]
