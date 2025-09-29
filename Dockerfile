FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 7860

# Default envs (can be overridden with -e in podman run)
ENV OLLAMA_HOST=localhost
ENV OLLAMA_PORT=11434
ENV MODEL=mistral-7b-instruct

CMD ["python", "app.py"]

