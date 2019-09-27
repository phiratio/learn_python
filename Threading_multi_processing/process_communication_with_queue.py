import multiprocessing

#SENTINEL = object() # no!
SENTINEL = 'STOP'   # not empty obj instance, bacuse id's get messed up


def producer(q, n):
    a, b = 0, 1
    while a <= n:
        q.put(a)
        a, b = b, a + b
    q.put(SENTINEL)


def consumer(q):
    while True:
        num = q.get()
        if num == SENTINEL:
            break
        print(f'Got numba {num}')


q = multiprocessing.Queue()  # not threading one
cns = multiprocessing.Process(target=consumer, args=(q, ))
prd = multiprocessing.Process(target=producer, args=(q, 35))

prd.start()
cns.start()