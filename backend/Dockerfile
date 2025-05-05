FROM python:3.10

# LABEL maintainer="Emiliano Rizzonelli <emiliano.rizzonelli@proton.me>"
# LABEL version="1.0"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn requests mysql-connector-python bcrypt python-multipart

EXPOSE 8000

# create a wait-for-it script
RUN echo '#!/bin/bash\n\
# wait for mysql to be ready\n\
while ! nc -z mysql 3306; do\n\
  echo "waiting for mysql..."\n\
  sleep 1\n\
done\n\
\n\
# wait a bit more to ensure mysql is fully ready\n\
sleep 5\n\
\n\
# initialize database\n\
python init_db.py\n\
\n\
# start the application\n\
uvicorn app:app --host 0.0.0.0 --port 8000' > /app/start.sh && \
chmod +x /app/start.sh

# install netcat for the wait-for-it script
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# run the startup script
CMD ["/app/start.sh"]
