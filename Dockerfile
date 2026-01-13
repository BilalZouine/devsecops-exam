# Image officielle Python légère et maintenue
FROM python:3.9-slim

# Empêche l’exécution en root (bonne pratique sécurité)
RUN useradd -m appuser

# Répertoire de travail
WORKDIR /app

# Copier uniquement les dépendances en premier (optimisation cache)
COPY api/requirements.txt .

# Installer les dépendances sans cache
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copier le code de l’application
COPY api/ .

# Changer l’utilisateur
USER appuser

# Port exposé
EXPOSE 5000

# Désactiver le mode debug via variable d’environnement
ENV FLASK_ENV=production

# Lancer l’application
CMD ["python", "app.py"]
