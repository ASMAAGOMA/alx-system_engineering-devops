#install flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# Ensure the correct version of Werkzeug is installed
package { 'Werkzeug':
  ensure   => '0.15.5', # or whichever version is compatible
  provider => 'pip3'
}