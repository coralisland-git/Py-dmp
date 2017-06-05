# README #

### Recommended server configuration ###

Ubuntu 14.04 LTS

Apache/2.4.7 (Ubuntu)

MySQL 5.5

### Apache/Mysql installation ###

```
#!

sudo apt-get update && sudo apt-get install apache2 mysql-server libapache2-mod-wsgi-py3

```

### Project source code ###
Clone project into apache web directory

```
#!

cd /var/www/html
sudo git clone https://<user>@bitbucket.org/axisbits/data-management-platform.git
```