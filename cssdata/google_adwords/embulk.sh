#!/bin/bash
export CSS_PATH=/var/www/html/data-management-platform/cssdata
/var/www/html/.virtualenvs/dmp/bin/python $CSS_PATH/google_adwords/pulling.py
/home/web-user/.embulk/bin/embulk run $CSS_PATH/google_adwords/embulk_config.yml
