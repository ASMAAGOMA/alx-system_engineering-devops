#install flask from pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask Werkzeug --upgrade',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
