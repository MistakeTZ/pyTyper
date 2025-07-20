FROM python:3.12-slim

# Установка Node.js
RUN apt-get update && \
    apt-get install -y curl gnupg git build-essential && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Установка tsserver и LSP
RUN npm install -g typescript typescript-language-server

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . /app
WORKDIR /app

# Открытие порта
EXPOSE 8000

# Запуск сервера
CMD ["uvicorn", "pyTyper.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
