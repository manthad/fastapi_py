FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev build-essential && \
    ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
