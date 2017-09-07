#!/bin/bash
/var/www/html/.virtualenvs/dmp/bin/python /var/www/html/data-management-platform/fb_ads/pulling.py -f /var/www/html/data-management-platform/fb_ads/credentials.json
/home/web-user/.embulk/bin/embulk run /var/www/html/data-management-platform/fb_ads/embulk_config.yml
