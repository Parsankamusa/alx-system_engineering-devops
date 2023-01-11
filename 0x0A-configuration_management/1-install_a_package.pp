# install puppet-lint -v 2.1.0

exec { 'puppet-lint':
  ensure=> '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
}
