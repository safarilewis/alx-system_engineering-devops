include stdlib
package { 'nginx':
  ensure => installed
}
file_line {'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server {',
  line   => 'add_header X-Served-By $hostname;'
}
service {'nginx':
  ensure  => running
}
