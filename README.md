# README #

### Recommended server configuration ###

Ubuntu 14.04 LTS

Apache/2.4.7 (Ubuntu)

MySQL 5.5

### Apache/Mysql installation ###

```
#!

sudo apt-get update && sudo apt-get install apache2 mysql-server libmysqlclient-dev libapache2-mod-wsgi-py3 

```

### Project source code ###
Clone project into apache web directory

```
#!

cd /var/www/html
sudo git clone https://<user>@bitbucket.org/axisbits/data-management-platform.git
```

### Python environment setup ###

Switch to apache web directory and create directory for environments:

```
#!

cd /var/www/html
sudo mkdir .virtualenvs && sudo chmod -R o+rwx .virtualenvs/
```
Install pip and virtualenv tools for python 3:

```
#!

sudo apt-get update && sudo apt-get install python3-pip && pip3 install virtualenv
```
Create and activate new virtual environment for project:

```
#!

virtualenv -p python3 .virtualenvs/dmp
source .virtualenvs/dmp/bin/activate
```