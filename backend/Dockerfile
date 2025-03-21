FROM python:3.10

# LABEL maintainer="Emiliano Rizzonelli <emiliano.rizzonelli@proton.me>"
# LABEL version="1.0"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn requests mysql-connector-python

EXPOSE 8000

# in here we run the uvicorn app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
