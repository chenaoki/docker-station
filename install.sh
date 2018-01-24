#!/bin/sh

sed "s/ARGHOST/$1/g" docker-station.py.org > docker-station.py
sed "s/ARGHOST/$1/g" docker-station.conf.org > docker-station.conf

mkdir /var/www/cgi-bin
cp docker-station.py /var/www/cgi-bin
chmod 705 /var/www/cgi-bin/docker-station.py

gpasswd -a www-data docker

cp docker-station.conf /etc/apache2/sites-available
a2enmod cgi
a2ensite docker-station
service apache2 restart
