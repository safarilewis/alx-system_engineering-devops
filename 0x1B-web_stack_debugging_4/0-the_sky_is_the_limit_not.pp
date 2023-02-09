#Allows multiple connections to the server.
exec { '/usr/bin/env sed -i s/15/2000/g /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }