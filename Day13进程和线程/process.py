# Python的os模块提供了fork()函数。
# 由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，
# 可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的封装，
# 例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()

    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()

    p1.join()
    p2.join()
    end = time()
    
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()