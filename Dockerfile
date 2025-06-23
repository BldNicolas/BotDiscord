FROM python:3.11

# Installe les outils de compilation nécessaires
RUN apt-get update && apt-get install -y build-essential

# Crée un dossier de travail
WORKDIR /app

# Copie requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

# Lance le bot
CMD ["python", "bot.py"]