#!/bin/bash

#absolute path will work as well
config_file=../config/config.ini
expected_config_vars=( host user port pass )

if [ ! -f $config_file ] 
then
    echo "Missing config file: $config_file"
    exit 1
fi
. $config_file

for var in ${expected_config_vars[@]} 
do
    if [ -z "${!var}" ]
    then
        echo "Missing config variable: $var"
        exit 1
    fi
done

echo $host $user $port $pass
