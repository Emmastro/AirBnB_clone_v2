#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Release test" >> /data/web_static/releases/test/index.html
# Create symlink, override if already exists
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/ 

# Add static location to nginx settings: 
sed -i '50 a \
location /hbnb_static/ {\
                alias /data/web_static/current/;\
                autoindex off;\
        }\
' /etc/nginx/sites-enabled/default

service nginx restart
