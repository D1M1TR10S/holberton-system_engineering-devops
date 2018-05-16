exec { 'Replacing phpp typo in wp-settings.php':
  path     => '/bin',
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}