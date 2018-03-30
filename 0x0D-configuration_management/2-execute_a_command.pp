# Killing a process named killmenow
exec { 'Terminate process: killmenow':
    command => 'pkill -f killmenow',
}
