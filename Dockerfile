FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --upgrade setuptools pip && pip3 install -r requirements.txt
COPY . .
