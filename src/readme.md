# Readme

## 1. pi settup

raspi-config setup

```sh
sudo raspi-config
# setup wifi with option 2
# setup ssh with option 5
# setup spi with option 5
```

reboot so that the config can take effect

```sh
sudo reboot
```

install git

```sh
sudo apt update
sudo apt install git
```

install venv

```sh
sudo apt-get update
sudo apt-get install python3-venv -y
```

clone repo

```sh
git clone <weather-repo>
```

create venv

```sh
cd <weather-repo>
python3 -m venv .venv
```

activate venv

```sh
source .venv/bin/activate
```

install packages from requirements.txt

```sh
pip install -r requirements.txt
```

run files from src dir

---

## 2. node setup

install node and npm  
credit to: https://github.com/sdesalas/node-pi-zero

```sh
#!/bin/bash
# By Steven de Salas

# Based on script by Richard Stanley @ https://github.com/audstanley/Node-MongoDb-Pi/
# This is for a RaspberryPi Zero but should work across all models.

VERSION=v11.15.0;

# Creates directory for downloads, and downloads node
cd ~/ && mkdir temp && cd temp;
wget https://nodejs.org/dist/$VERSION/node-$VERSION-linux-armv6l.tar.gz;
tar -xzf node-$VERSION-linux-armv6l.tar.gz;
# Remove the tar after extracing it.
sudo rm node-$VERSION-linux-armv6l.tar.gz;
# This line will clear existing nodejs
sudo rm -rf /opt/nodejs;
# This next line will copy Node over to the appropriate folder.
sudo mv node-$VERSION-linux-armv6l /opt/nodejs/;
# Remove existing symlinks
sudo unlink /usr/bin/node;
sudo unlink /usr/sbin/node;
sudo unlink /sbin/node;
sudo unlink /usr/local/bin/node;
sudo unlink /usr/bin/npm;
sudo unlink /usr/sbin/npm;
sudo unlink /sbin/npm;
sudo unlink /usr/local/bin/npm;
# Create symlinks to node && npm
sudo ln -s /opt/nodejs/bin/node /usr/bin/node;
sudo ln -s /opt/nodejs/bin/node /usr/sbin/node;
sudo ln -s /opt/nodejs/bin/node /sbin/node;
sudo ln -s /opt/nodejs/bin/node /usr/local/bin/node;
sudo ln -s /opt/nodejs/bin/npm /usr/bin/npm;
sudo ln -s /opt/nodejs/bin/npm /usr/sbin/npm;
sudo ln -s /opt/nodejs/bin/npm /sbin/npm;
sudo ln -s /opt/nodejs/bin/npm /usr/local/bin/npm;
```

install pm2

```sh
sudo npm install -g pm2
sudo ln -s /opt/nodejs/bin/pm2 /usr/bin/pm2
```

run weather in pm2 from ~

```sh
cd ~
pm2 start ./weather/src/weather.py --interpreter ./weather/.venv/bin/python
```

start up on reboot

```sh
pm2 startup
# copy and paste the startup command

pm2 save
```

<!-- TODO -->
<!-- create ecosystem file -->
