import threading
import time 

# reference : https://blog.csdn.net/brucewong0516/article/details/81028716

# def thread_1():
#     print('当前线程 %s 正在运行' % threading.current_thread().name)
#     time.sleep(1)
#     print('当前线程 %s 结束运行' % threading.current_thread().name)

# print('当前线程 %s 正在运行' % threading.current_thread().name)
# t1 = threading.Thread(target=thread_1, args=[])

# t1.start()
# print('当前线程 %s 结束运行' % threading.current_thread().name)

################################ 输出如下 ################################
'''
    当前线程 MainThread 正在运行
    当前线程 Thread-1 (thread_1) 正在运行
    当前线程 MainThread 结束运行
    当前线程 Thread-1 (thread_1) 结束运行
'''

# 为了让自线程在主线程之前结束，调用join()方法

# def thread_1():
#     print('当前线程 %s 正在运行' % threading.current_thread().name)
#     time.sleep(1)
#     print('当前线程 %s 结束运行' % threading.current_thread().name)

# print('当前线程 %s 正在运行' % threading.current_thread().name)
# t1 = threading.Thread(target=thread_1, args=[])

# t1.start()
# t1.join() # 阻塞线程， join实现的功能是线程同步，主线程任务结束之前，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止。
# print('当前线程 %s 结束运行' % threading.current_thread().name)

################################ 输出如下 ################################
'''
    当前线程 MainThread 正在运行
    当前线程 Thread-1 (thread_1) 正在运行
    当前线程 Thread-1 (thread_1) 结束运行
    当前线程 MainThread 结束运行
'''


# 设置守护进程

# def run():

#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)


# if __name__ == '__main__':

#     start_time = time.time()

#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)

#     for t in thread_list:
#         t.demon = True
#         t.start()

#     print('主线程结束了！' , threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)


################################ 输出如下 ################################
'''
    这是主线程： MainThread
    主线程结束了！ MainThread
    一共用时： 0.0009453296661376953
    # NOTE: 主线程结束后子线程依旧在运行 未加join()
    当前线程的名字是：  Thread-1 (run)
    当前线程的名字是：  Thread-2 (run)
    当前线程的名字是：  Thread-3 (run)
    当前线程的名字是：  Thread-4 (run)
    当前线程的名字是：  Thread-5 (run)
'''

def target():
    print('当前的线程%s 在运行' % threading.current_thread().name)
    time.sleep(4)
    print('当前的线程 %s 结束' % threading.current_thread().name)
 
print('当前的线程 %s 在运行' % threading.current_thread().name)
t = threading.Thread(target=target,args = [])

t.daemon = False
t.start()
t.join(5)  #为子线程设定运行的时间，5s后就退出子线程，如果不加等待时间，就会一直等待子线程运行结束后，再运行主线程
print('当前的线程 %s 结束' % threading.current_thread().name)

################################ 输出如下 ################################
'''
    当前的线程 MainThread 在运行
    当前的线程Thread-1 (target) 在运行
    当前的线程 Thread-1 (target) 结束
    当前的线程 MainThread 结束
    # NOTE: 主线程结束后子线程就结束了 添加join()
'''