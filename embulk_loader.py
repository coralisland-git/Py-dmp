#!/usr/bin/python
import os
from subprocess import call

print("Searching files to process.")

# locate all files within given path(root directory and it's subdirs)
for dirpath, dirnames, filenames in os.walk("/var/www/html/data-management-platform/dmp/data_loader/embulk_configs/providers"):

    # search for all config files (with yml extension)
    for filename in [f for f in filenames if f.endswith(".yml")]:
        file_path = os.path.join(dirpath, filename)
        print("Processing file: "+file_path)

        try:
            # embulk script invocation
            # embulk_home_path - path to directory where embulk has been installalled and configured with it's environment
            # config_file - file with configuration for particular user/provider
            result_code = call(". {embulk_home_path}.bashrc; {embulk_home_path}.embulk/bin/embulk run {config_file}".format(embulk_home_path='/home/web-user/', config_file=file_path), shell=True)
            if result_code == 0:
                print('Data has been loaded successfully')
            else:
                print('Data loading has been failed')
        except:
            print('Data loading has been failed')
