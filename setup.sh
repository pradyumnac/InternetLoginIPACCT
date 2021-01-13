#!/usr/bin/env bash

# Add virtualenv

# create log directory

# setup pasword in .env file from sample.env

# add entry in crontab
(crontab -l | grep '/scripts/ipacct/run.sh') || { crontab -l; echo '0 * * * * ./scripts/ipacct/run.sh'; } | crontab -
# echo "0 * * * * ./scripts/ipacct/run.sh"
