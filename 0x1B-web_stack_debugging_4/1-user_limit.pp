#Deleting user limit for holberton
exec { '/usr/bin/env sed -i s/holberton.*//g /etc/security/limits.conf': }