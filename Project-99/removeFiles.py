import os
import shutil
import time

path = "C:/Users/Dell/Downloads/Project-99/Deleting files"
days = 10
seconds = time.time()

if os.path.exists(path):
    for files in os.walk(path):
        ctime = os.stat(path).st_ctime
        if ctime < seconds:
            shutil.rmtree(path)      
