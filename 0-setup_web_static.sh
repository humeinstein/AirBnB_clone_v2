#!/usr/bin/env bash     
# saetup nginx && create index.html &&
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e "
<html>
  <head>
    <title>Wow</title>
  </head>
  <body>
     <p>WOW!</p>
  </body>
</html>
" | sudo tee -a /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "42i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
