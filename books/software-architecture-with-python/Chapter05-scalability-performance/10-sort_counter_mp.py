# Code Listing #10

"""

Sort a number of disk files using a counter using multiple processes
Bottleneck here is the processing time it takes to load the files into memory –
in file I/O - not the computation (sorting), as the sorting is just an increment
in the counter. Hence the single process version is pretty efficient as it is able
to load all the file data in the same address space. The multiple-process ones are
able to improve this a bit by loading the files in multiple address spaces, but not by a lot.
"""

# 10-sort_counter_mp.py
import sys
import collections
from multiprocessing import Pool

MAXINT = 100000


def sorter(filenames):
    """ Sorter process sorting files using a counter """

    counter = collections.defaultdict(int)

    for filename in filenames:
        for i in open(filename):
            counter[i] += 1

    return counter


def batch_files(pool_size, limit):
    """ Create batches of files to process by a multiprocessing Pool """

    batch_size = limit // pool_size

    filenames = []

    for i in range(pool_size):
        batch = []
        for j in range(i * batch_size, (i + 1) * batch_size):
            filename = 'numbers/numbers_%d.txt' % j
            batch.append(filename)

        filenames.append(batch)

    return filenames


def sort_files(pool_size: int, filenames: list):
    """ Sort files by batches using a multiprocessing Pool """

    with Pool(pool_size) as pool:
        counters = pool.map(sorter, filenames)

        with open('sorted_nums.txt', 'w') as fp:
            for i in range(1, MAXINT + 1):
                count = sum([x.get(str(i) + '\n', 0) for x in counters])
                if count > 0:
                    fp.write((str(i) + '\n') * count)

        print('Sorted')


if __name__ == "__main__":
    limit_num = int(sys.argv[1])
    pool_size_num = 4

    filenames_list = batch_files(pool_size_num, limit_num)
    sort_files(pool_size_num, filenames_list)
