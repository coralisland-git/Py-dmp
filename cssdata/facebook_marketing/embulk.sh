#!/bin/bash
export CSS_PATH=/var/www/html/data-management-platform/cssdata
/var/www/html/.virtualenvs/dmp/bin/python $CSS_PATH/facebook_marketing/pulling.py -f $CSS_PATH/facebook_marketing/credentials.json
/home/web-user/.embulk/bin/embulk run $CSS_PATH/facebook_marketing/embulk_config.yml
