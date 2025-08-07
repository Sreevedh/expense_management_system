FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

COPY . /app

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]