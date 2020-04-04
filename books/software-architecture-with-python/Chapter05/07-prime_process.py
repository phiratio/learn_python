# Code Listing #7

"""
Primality checker - using multiple processes

Run this as,

$ time python3 07-prime_process.py > /dev/null

"""

import multiprocessing
from queue import Queue, Empty


def is_prime(n):
    """ Check for input number primality """

    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            print(n, 'is not prime')
            return False

    print(n, 'is prime')
    return True


if __name__ == "__main__":
    NUMBERS = [1297337, 1116281, 104395303,
               472882027, 533000389, 817504243,
               982451653, 112272535095293,
               115280095190773, 1099726899285419] * 100

    POOL = multiprocessing.Pool(4)
    POOL.map(is_prime, NUMBERS)
