FROM python:3.11-slim

# Installare dipendenze di sistema
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Setta variabili d'ambiente per Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Setta la directory di lavoro
WORKDIR /app

# Copia tutti i file nel container
COPY . .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r blinker==1.6.2

# Esponi la porta 8000
EXPOSE 8000

# Comando per avviare l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
