from multiprocessing import Process
import random
import string
import hashlib
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def sha256(z):
    hashlib.sha256(z)
def f():
    for x in range(0, 1000):
        for x in range(0, 1000):
            rand_string = random_char(x)
            sha256(rand_string)
            print sha256
if __name__ == 'main':
    p = Process(target=f)
    for i in range(0, 100):
        p.start()
        print "Thread Started"
    p.join()
