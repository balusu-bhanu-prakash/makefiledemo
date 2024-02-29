FROM python:3.12

WORKDIR /E1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /E1

CMD ["python", "add.py"]
