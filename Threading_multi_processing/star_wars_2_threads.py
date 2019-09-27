import threading
from time import sleep
from random import random


def run(n):
    t = threading.current_thread()
    for count in range(n):
        print(f'Hello from {t.name}! ({count})')
        sleep(0.9 * random())


yoda = threading.Thread(target=run, name='Yoda', args=(4, ))
vader = threading.Thread(target=run, name='Vader', args=(3, ))
yoda.start()
vader.start()
yoda.join()
vader.join()
