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
Install dependencies for project into virtual environment:

```
#!

pip3 install -r /var/www/html/data-management-platform/dmp/requirements.txt
```

### Virtual host setup ###
Update default apache hosts configuration file (000-default.conf)


```
#!

cd /etc/apache2/sites-available
sudo cp 000-default.conf 000-default.conf.backup
sudo touch dmp.conf 
sudo nano dmp.conf
```

Paste listed configuration into dmp.conf and save:

```
#!

<VirtualHost *:80>

       WSGIScriptAlias / /var/www/html/data-management-platform/dmp/wsgi.py

       <Directory /var/www/html/data-management-platform/dmp/>
                <Files wsgi.py>
                       Require all granted
                </Files>
        </Directory>

        Alias /static/ /var/www/html/data-management-platform/dmp/dmp/static/
        Alias /favicon.ico /var/www/html/data-management-platform/dmp/dmp/static/images/favicon.ico
        Alias /media/ /var/www/html/data-management-platform/dmp/dmp/media/

        <Location "/static/">
                Options -Indexes
        </Location>
        <Directory /var/www/html/data-management-platform/dmp/dmp/static>
                Require all granted
        </Directory>
        <Location "/media/">
                Options -Indexes
        </Location>
 <Directory /var/www/html/data-management-platform/dmp/dmp/media>
                Require all granted
        </Directory>
</VirtualHost>
```
Replace defult configuration with updated content and restart web-server:

```
#!


sudo cp dmp.conf 000-default.conf
sudo service apache2 restart
```