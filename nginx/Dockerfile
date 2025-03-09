FROM nginx:latest

# LABEL maintainer="Emiliano Rizzonelli <emiliano.rizzonelli@proton.me>"
# LABEL version="1.0"

COPY nginx/benchai.conf /etc/nginx/conf.d/default.conf

COPY frontend/* /var/www/html/

# exposing both http and https...
EXPOSE 80 443