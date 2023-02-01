# Changing the wrong extension "phpp" to php.
exec {'/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php':}

