# !/usr/bin/env/python
from multiprocessing.pool import ThreadPool
import time
import threading
import os
import sys

def target_func():
    count=int(sys.argv[2])
    while count>0:
        os.system('dgx job submit -f caffe_dm.json')
        count=count-1

print(sys.argv[1])
array=[]
for i in range(0, int(sys.argv[1])):
    t=threading.Thread(target=target_func)
    array.append(t)
    t.start()

for j in range(0, int(sys.argv[2])):
    array[j].join()
