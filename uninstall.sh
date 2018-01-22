rm /var/www/cgi-bin/docker-station.py 

rm /etc/apache2/sites-available/docker-station.conf 

gpasswd -d www-data docker

a2dissite docker-station
service apache2 restart
