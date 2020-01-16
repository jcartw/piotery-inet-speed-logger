
# Installs
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install vim
sudo apt-get install git
sudo apt-get install python3-pip

# Installing Python 3.7.4
https://installvirtual.com/install-python-3-7-on-raspberry-pi/

# PIP Installs
pip3 install virtualenv

# Setup Virtual Env
cd /home/pi/piotery-inet-speed-logger
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Setup .env file with ENVs
```
export DARKSKY_API_KEY=DARKSKY_API_KEY
export LATITUDE=LATITUDE
export LONGITUDE=LONGITUDE

export IOTERY_DEVICE_KEY=IOTERY_DEVICE_KEY
export IOTERY_DEVICE_SERIAL=IOTERY_DEVICE_SERIAL
export IOTERY_DEVICE_SECRET=IOTERY_DEVICE_SECRET
export IOTERY_TEAM_UUID=IOTERY_TEAM_UUID
```

# Update /etc/rc.local file
* see reference file here

