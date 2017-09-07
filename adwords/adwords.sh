#!/bin/bash
/var/www/html/.virtualenvs/dmp/bin/python /var/www/html/data-management-platform/adwords/get_data.py
/home/web-user/.embulk/bin/embulk run /var/www/html/data-management-platform/adwords/adwords.yml
