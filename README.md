# Raspotify Status
A simple monitoring app for the awesome [raspotify client](https://github.com/dtcooper/raspotify) on raspbian

![](/screenshot.png?raw=true)

## Introduction
raspotify-monitor is not a very advanced application, it was written in a hurry, executes bash commands and does even worse things so all contributions are welcome.
The motivation behind writing this was that librespot was crashing so often that it got annoying to restert raspotify manually.

## Checks
**✔ Service Running** states that the service is active and running

**✔ Listening** states that the serivice is listening on one or more ports

**✔ Connection Established** states that the server has established one or more connections

## Installation
### Fast
Open a new ssh session to the raspotify host and navigate to your home directory then run the following command

⚠️ deletes existing installations ⚠️
```bash
wget -qO- https://github.com/manzari/raspotify-monitor/raw/master/install/install.sh | bash
```
### Manual
#### Requirements
```bash
sudo apt-get install -y python3-pip nginx
sudo -H pip3 install -r requirements.txt
```
#### Copy config files
```bash
sudo cp nginx.conf /etc/nginx/nginx.conf
sudo cp gunicorn.service /etc/systemd/system/gunicorn.service
```
#### Start the services
```bash
sudo systemctl daemon-reload
sudo service gunicorn start
sudo service nginx start
```
