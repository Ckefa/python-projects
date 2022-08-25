from time import time

tm = time()
nm = 499_999
def search(a, b):
    for i in range(a, b):
        print(i)
        if i == nm:
            return i

n = search(0, 500_000)
print(f"PSK: {n} - Time consumed: {round(time() - tm, 8)} seconds")

