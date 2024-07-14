#!/usr/bin/env bash
# Setup a web servers for the deployment of web_static.
sudo apt-get update -y
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
   <p>Nginx server test</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
