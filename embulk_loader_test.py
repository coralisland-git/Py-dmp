#!/usr/bin/python
import os
from multiprocessing import Process, Queue
from subprocess import call, check_output, CalledProcessError

def cmdloop(inQueue,outQueue):
    while True:
        command = inQueue.get()
        try:
            result = call(command, shell=True)
        except CalledProcessError as e:
            result = e

        outQueue.put(result)

inQueue = Queue()
outQueue = Queue()
cmdHostProcess = Process(target=cmdloop, args=(inQueue,outQueue,))
cmdHostProcess.start()

def callCommand(command):
    inQueue.put(command)
    return outQueue.get()

def killCmdHostProcess():
    cmdHostProcess.terminate()


from subprocess import call
print("Searching files to process.")
for dirpath, dirnames, filenames in os.walk("/var/www/html/data-management-platform/dmp/data_loader/embulk_configs/providers"):

    for filename in [f for f in filenames if f.endswith(".yml")]:
        file_path = os.path.join(dirpath, filename)
        print("Processing file: "+file_path)
        # log_file = open(os.path.join('/home/web-user/logs', 'embulk_stdout.log'), "w+")
        try:
            result_code = callCommand(". {embulk_home_path}.rvm/scripts/rvm; {embulk_home_path}.embulk/bin/embulk run {config_file}".format(embulk_home_path='/home/web-user/', ))
            if result_code == 0:
                print('Data has been loaded successfully')
            else:
                print('Data loading has been failed')
        except:
            print('Data loading has been failed')
