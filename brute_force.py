from time import time
import math,pdb
from   collections import Counter

counter = Counter([3,4,5,6,7,3,5,34,5,7,7,7,7,7,7,7,5,5,54,39,3])
print(counter.most_common()[-1][0])

ST = 0
tm = time()

def mid_val(a, b):
    global ST
    ST += 1
   #print(a, b)
    mid = (a + b) // 2
    pdb.set_trace()
    print(mid)

    if mid == NM:
        found(mid)
    elif NM == a:
        found(a)
    elif NM == b:
        found(b)
    elif b > a + 1:
        mid_val(a, (mid - 1))
        mid_val((mid + 1), b)
    else:
        pass
def found(VAL):
    print(f"R.PSK: {VAL}\ntime: {round(time() - tm, 5)}\nsteps: {ST}")
    exit()

NM = 49_999
mid_val(0, 500_000)


#    1  2  3  4  5 6 7 8 9  10

