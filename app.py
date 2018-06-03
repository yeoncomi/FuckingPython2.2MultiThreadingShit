from threading import Thread
import random
import string
import hashlib
import time
start_time = time.time()
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def sha256(z):
    fivetwelve = hashlib.sha512(z)
    return hashlib.sha512(str(fivetwelve.hexdigest()))
def f():
    for x in range(0, 1000000):
        for x in range(0, 1000000):
            rand_string = random_char(x)
            return sha256(rand_string)
thread = Thread(target = f)
thread_list = []
for i in range(0, 10000):
    t = Thread(target=f)
    thread_list.append(t)
for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()
time = (time.time()-start_time)
print "finished in "+str(time)+"Seconds"