<?php
$iniPath = 'config.ini';
$expectedVariables = array('host', 'port', 'user', 'pass');

if (!is_readable($iniPath)) {
    die("Missing config file: $iniPath\n");
}
$config = parse_ini_file($iniPath);
if (!$config) {
    die("Empty or invalid config file \n");
}
foreach ($expectedVariables as $var) {
    if (!isset($config[$var])) {
        die("Missing config variable: $var\n");
    }
}
echo $config['user'] . "\n";
echo $config['host'] . "\n";
echo $config['pass'] . "\n";
echo $config['port'] . "\n";
