import multiprocessing
from multiprocessing import Process, Queue # multiprocessing.Manager.Queue
import time

class Citizen(Process):
    def __init__(self, queue, people, v):
        Process.__init__(self)
        self.queue = queue
        self.people = people
        self.v = v

    def pay(self, people, v):
        for i in range(v):
            people.append(v)
        return people

    def run(self):
        temp = self.pay(self.people, self.v)
        self.queue.put(temp)



if __name__ == '__main__':
    citizens, res = [], []
    queue = Queue()
    people, proc, v = [], 4, 10_000_000

    st = time.time()

    for _ in range(proc):
        citizens.append(Citizen(queue, people, v))
    for i in citizens:
        i.start()

    while proc:
        res += queue.get()
        print(len(res))
        proc -= 1
    
    nd = time.time()

    print(f"Time: {nd - st}")






