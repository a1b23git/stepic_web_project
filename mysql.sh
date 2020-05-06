#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
