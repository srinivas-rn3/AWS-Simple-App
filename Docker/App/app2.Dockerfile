
FROM nginx:latest

RUN mkdir -p /usr/share/nginx/html/app2/

WORKDIR /etc/nginx/conf.d
COPY default.conf default.conf

WORKDIR /usr/share/nginx/html/app2/
COPY index.html index.html
