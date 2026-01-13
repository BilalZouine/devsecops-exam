FROM python:3.9-slim

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "app.py"]
