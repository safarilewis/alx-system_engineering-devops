# Creates a file in tmp
file {'/tmp/school':
     content => 'I love Puppet'
     group => 'www-data'
     owner => 'www-data'
     permission => '0744'
}
