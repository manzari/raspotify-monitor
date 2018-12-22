#!/usr/bin/bash
sudo apt-get update
sudo apt-get install -y python3-pip nginx
if test "$PWD" = "/home/pi"; then
        if test -d /home/pi/raspotify-monitor; then
            sudo service gunicorn stop
            sudo service nginx stop
            sudo rm -r /home/pi/raspotify-monitor
        fi
    echo downloading repo... >&2
    wget https://github.com/manzari/raspotify-monitor/archive/master.zip
    unzip master.zip
    rm master.zip
    mv raspotify-monitor-master raspotify-monitor
else
    echo ERROR: must be executed in /home/pi >&2
    exit 1
fi
sudo -H pip3 install -r raspotify-monitor/install/requirements.txt
sudo cp raspotify-monitor/install/nginx.conf /etc/nginx/nginx.conf
sudo cp raspotify-monitor/install/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo service gunicorn start
sudo service nginx start
echo done! >&2
exit 0