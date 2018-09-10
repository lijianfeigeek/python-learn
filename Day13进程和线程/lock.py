# 我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，
# 而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，
# 其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。
# 下面的代码演示了如何使用“锁”来保护对银行账户的操作，从而获得正确的结果。

# 比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，
# 这一点只要启动几个执行死循环的线程就可以得到证实了。
# 之所以如此，是因为Python的解释器有一个“全局解释器锁”（GIL）的东西，
# 任何线程执行前必须先获得GIL锁，然后每执行100条字节码，
# 解释器就自动释放GIL锁，让别的线程有机会执行，这是一个历史遗留问题，
# 但是即便如此，就如我们之前举的例子，使用多线程在提升执行效率和改善用户体验方面仍然是有积极意义的。

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


# 现代操作系统对I/O操作的改进中最为重要的就是支持异步I/O。
# 如果充分利用操作系统提供的异步I/O支持，就可以用单进程单线程模型来执行多任务，
# 这种全新的模型称为事件驱动模型。Nginx就是支持异步I/O的Web服务器，
# 它在单核CPU上采用单进程模型就可以高效地支持多任务。
# 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），
# 充分利用多核CPU。用Node.js开发的服务器端程序也使用了这种工作模式，这也是当下实现多任务编程的一种趋势。

# 在Python语言中，单线程+异步I/O的编程模型称为协程，
# 有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
# 协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，
# 而是由程序自身控制，因此，没有线程切换的开销。
# 协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，
# 也不存在同时写变量冲突，在协程中控制共享资源不用加锁，只需要判断状态就好了，
# 所以执行效率比多线程高很多。如果想要充分利用CPU的多核特性，最简单的方法是------------>多进程+协程，
# 既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。


# 1. 将耗时间的任务放到线程中以获得更好的用户体验。
# 2. 使用多进程对复杂任务进行“分而治之”。
