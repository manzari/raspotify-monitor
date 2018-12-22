# Raspotify Status
A simple monitoring app for the awesome [raspotify client](https://github.com/dtcooper/raspotify) on raspbian

![](/screenshot.png?raw=true)

## Installation
### Fast
Open a new ssh session to the raspotify host and navigate to your home directory then run the following command
```bash
wget -qO- https://github.com/manzari/raspotify-monitor/raw/master/install/install.sh | bash
```
### Manual
#### Requirements
```bash
sudo apt-get install -y python3-pip nginx
sudo -H pip3 install -r requirements.txt
```
#### Download and extract files
Not that you can also install older [releases](https://github.com/manzari/raspotify-monitor/releases) instead of the latest master
```bash
    wget https://github.com/manzari/raspotify-monitor/archive/master.zip
    unzip master.zip
    rm master.zip
    mv raspotify-monitor-master raspotify-monitor

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