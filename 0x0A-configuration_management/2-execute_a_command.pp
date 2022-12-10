#Executes a command
exec {'Kill a Process':
     command => 'usr/bin/pkill -f killmenow',
}