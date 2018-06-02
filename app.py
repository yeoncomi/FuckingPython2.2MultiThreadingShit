from multiprocessing import Process
import random
import string
import hashlib
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def sha256(z):
    return hashlib.sha256(z)
def f():
    for x in range(0, 10000000):
        for x in range(0, 100000):
            rand_string = random_char(x)
            return sha256(rand_string)
p = Process(target=f)
for i in range(0, 100):
    p.start()
    print "Thread Started"
p.join()
