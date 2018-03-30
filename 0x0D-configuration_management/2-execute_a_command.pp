# Killing a process using puppet
exec { "killmenow":
    command => "/usr/bin/pkill -f killmenow",
    provider => 'shell',
}
