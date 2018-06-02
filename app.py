from multiprocessing import Process

def f():
    for x in range(0, 100000000):
        for x in range(0, 100000000):
            z=z+1
if name == 'main':
    p = Process(target=f)
    for i in range(0, 100):
        p.start()
    p.join()
