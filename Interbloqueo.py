
from threading import Thread
from threading import Lock

g_num=0
def work1():
    global g_num
    for i in range(1000000):
        mutex.acquire () # Bloquear
        g_num+=1
        mutex.release () # Desbloquear
    print('1g_num:', g_num)
def work2():
    global g_num
    for i in range(1000000):
        mutex.acquire () # Bloquear
        g_num+=1
        mutex.release () # Desbloquear
    print('2g_num:', g_num)

mutex = Lock () # Crea un objeto de bloqueo
if __name__ == '__main__':
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print('g_num:', g_num)