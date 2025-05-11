import random

from List import List


class Queue(List):
    def enqueue(self, e):
        self.insertAsLast(e)

    def dequeue(self):
        return self.remove(self.first())

    @property
    def front(self):
        return self.first().data

    def __repr__(self):
        return '<Queue({})>'.format(','.join([str(i) for i in self]))


class Customer:
    def __init__(self, window, time):
        self.window = window
        self.time = time

    def __repr__(self):
        return '<Customer window={} time={}>'.format(self.window, self.time)


def bestWindow(windows: list, nWin: int):
    """查找排队人数最少的那个队列窗口"""
    minSize = windows[0].size()
    optiWin = 0
    for i in range(nWin):
        if minSize > windows[i].size():
            minSize = windows[i].size()
            optiWin = i
    return optiWin


def simulate(nWin, servTime):
    """
        >>> simulate(10, 10)
    """
    windows = []
    for _ in range(nWin):
        windows.append(Queue())
    for _ in range(servTime):
        if random.random() % (1 + nWin):
            bestWin = bestWindow(windows, nWin)
            time = 1 + random.random() % 98
            c = Customer(bestWin, time)
        windows[c.window].enqueue(c)
    for i in range(nWin):
        if not windows[i].empty():
            windows[i].front.time -= 1
            if windows[i].front.time <= 0:
                windows[i].dequeue()
    print(windows)
    del windows
