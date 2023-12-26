# 在多线程的应用下，如何保证线程安全，以及线程之间的同步，或者访问共享变量都是十分棘手的问题
# python中提供了Lock、Rlock、Semaphore、Event、Condition来保证线程之间的同步
# Lock & RLock ： 互斥锁，用来保证多线程访问共享变量的问题
# Semaphore对象：Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程拥有
# Event对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其区执行操作
# Condition对象：其可以在某些事件触发或者达到特定的条件后才处理数据

# reference: https://blog.csdn.net/brucewong0516/article/details/81050939

#################### 1 Lock ####################

# 不使用锁
import threading
import time

# num = 0

# def show(arg):
#     global num
#     time.sleep(1)
#     num += 1
#     print('bb:{}'.format(num))

# for i in range(5):
#     t = threading.Thread(target=show, args=(i,)) # 注意传入参数后一定要有逗号
#     t.start()

# print('main thread stop')

#################### 输出 ####################
'''
    main thread stop
    bb:1
    bb:2
    bb:3
    bb:4
    bb:5
'''

# 使用锁

# NOTE: 对于普通的Lock而言，如果一个线程连续两次release,会使得线程死锁
# 所以Lock不常用，一般采用RLock进行线程锁的设定
num = 0
lock = threading.RLock()

def Func():
    # 此处添加锁是为了保护全局变量num
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    print("num == {}".format(num))
    lock.release()

for i in range(10):
    t = threading.Thread(target=Func)
    t.start()