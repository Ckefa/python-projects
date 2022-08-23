import multiprocessing as mp
import time

a, b, c = [], [], []

def app1(m):
    for i in m:
        a.append(i)

def app2(m):
    for i in m:
        b.append(i)

def app3(m):
    for i in m:
        c.append(i)


if __name__ == '__main__':
    numbs = list(range(8_000_000))

    st = time.time()
    app1(numbs)
    app2(numbs)
    app3(numbs)
    nd = time.time()

    print(f"serial time: {nd - st}")
    
    p1 = mp.Process(target = app1, args=(numbs,))
    p2 = mp.Process(target = app2, args=(numbs,))
    P3 = mp.Process(target = app3, args=(numbs,))

    st = time.time()
    p1.start()
    p2.start()
    P3.start()
    nd = time.time()

    print(f"parallel time: {nd - st}")

    print(len(a), len(b), len(c))

