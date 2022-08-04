#!/bin/bash

# turn on bash's job control
set -m

# extract environment variables for cron
printenv | sed 's/^\(.*\)$/export \1/g' |  sed -e 's/[()&!]/\\&/g' > /root/project_env.sh
chmod +x /root/project_env.sh

# Start the helper processes
service rsyslog start
service cron start

crontab cron/crontab

tail -f /dev/null