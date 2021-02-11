# Readme

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



