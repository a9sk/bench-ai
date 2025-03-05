#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

set -e  # we do not want any errors during setup

# install dependencies
echo -e "${GREEN}[+][+][+][+] installing dependencies [+][+][+][+]${NC}"
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv nginx ufw certbot python3-certbot-nginx

# activate virtual environment
echo -e "${GREEN}[+][+][+][+] activating venv [+][+][+][+]${NC}"
python3 -m venv venv
source venv/bin/activate

# install and start backend
echo -e "${GREEN}[+][+][+][+] installing uvicorn [+][+][+][+]${NC}"
pip install --upgrade pip
pip install fastapi uvicorn requests

cd backend || exit

echo -e "${GREEN}[+][+][+][+] starting the backend [+][+][+][+]${NC}"
uvicorn app:app --host 127.0.0.1 --port 8000 --reload &

cd ..

# install and start frontend
echo -e "${GREEN}[+][+][+][+] configuring nginx [+][+][+][+]${NC}"
cp nginx/benchai.conf /etc/nginx/sites-available/benchai
ln -s /etc/nginx/sites-available/benchai /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

echo -e "${GREEN}[+][+][+][+] copy frontend to nginx path [+][+][+][+]${NC}"
cp -r frontend/* /var/www/html/
chmod -R 755 /var/www/html

# setup systemd service
echo -e "${GREEN}[+][+][+][+] setting up systemd [+][+][+][+]${NC}"
cp systemd/benchai.service /etc/systemd/system/benchai.service

# start the service
echo -e "${GREEN}[+][+][+][+] starting the service [+][+][+][+]${NC}"
systemctl daemon-reload
systemctl enable benchai
systemctl start benchai
systemctl status benchai

# ssl certificate
echo -e "${GREEN}[+][+][+][+] setup let's encrypt ssl [+][+][+][+]${NC}"
certbot --nginx -d 79.50.111.73 --non-interactive --agree-tos -m benchai.info@proton.me

# we are donezo
clear
echo -e "${GREEN}[+][+][+][+] setup complete [+][+][+][+]${NC}"
echo "access the site at: http://79.50.111.73/"
echo "backend API at: http://79.50.111.73/api/"
