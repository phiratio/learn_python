# Code Listing #4

"""

Thumbnail producer/consumer - Limiting number of images using a Semaphore.

A semaphore is initialized with a value greater than zero:

1. When a thread calls acquire on a semaphore that has a positive internal value, the value gets decremented by one,
and the thread continues on its way.
2. When another thread calls release on the semaphore, the value is incremented by 1.
3. Any thread calling acquire once the value has reached zero is blocked on the semaphore till it is woken up by another
thread calling release.
"""

import glob
import os
import random
import string
import threading
import time
import urllib.request
import uuid
from queue import Queue
from PIL import Image


class ThumbnailURL_Generator(threading.Thread):
    """ Worker class that generates image URLs """

    def __init__(self, queue, sleep_time=1, ):
        self.id = uuid.uuid4().hex
        self.sleep_time = sleep_time
        self.queue = queue
        # A flag for stopping
        self.flag = True
        # sizes
        self._sizes = (240, 320, 360, 480, 600, 720)
        # URL scheme
        self.url_template = 'https://dummyimage.com/%s/%s/%s.jpg'
        threading.Thread.__init__(self, name=f'producer-{self.id}')

    def __str__(self):
        return 'Producer'

    def get_size(self):
        return '%dx%d' % (random.choice(self._sizes),
                          random.choice(self._sizes))

    def get_color(self):
        return ''.join(random.sample(string.hexdigits[:-6], 3))

    def run(self):
        """ Main thread function """

        while self.flag:
            # generate image URLs of random sizes and fg/bg colors
            url = self.url_template % (self.get_size(),
                                       self.get_color(),
                                       self.get_color())
            # Add to queue
            print(self, 'Put', url)
            self.queue.put(url)
            time.sleep(self.sleep_time)

    def stop(self):
        """ Stop the thread """

        self.flag = False


class ThumbnailImageSemaSaver(object):
    """ Class which keeps an exact counter of saved images
    and restricts the total count using a semaphore """

    def __init__(self, limit=10):
        self.limit = limit
        self.counter = threading.BoundedSemaphore(value=limit)
        self.count = 0
        # Start time
        self.start = time.time()
        # Image saving rate
        self.rate = 0

    def acquire(self):
        # Acquire counter, if limit is exhausted, it
        # returns False
        return self.counter.acquire(blocking=False)

    def release(self):
        # Release counter, incrementing count
        return self.counter.release()

    def thumbnail_image(self, url, size=(64, 64), format='.png'):
        """ Save image thumbnails, given a URL """

        im = Image.open(urllib.request.urlopen(url))
        # filename is last two parts of URL minus extension + '.format'
        pieces = url.split('/')
        filename = ''.join((pieces[-2], '_', pieces[-1].split('.')[0], format))
        try:
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(filename)
            print('Saved', filename)
            self.count += 1
        except Exception as e:
            print('Error saving URL', url, e)
            # Image can't be counted, increment semaphore
            self.release()

        return True

    def save(self, url):
        """ Save a URL as thumbnail """

        if self.acquire():
            self.thumbnail_image(url)
            return True
        else:
            print('Semaphore limit reached, returning False')
            return False


class ThumbnailURL_Consumer(threading.Thread):
    """ Worker class that consumes URLs and generates thumbnails """

    def __init__(self, queue, saver):
        self.queue = queue
        self.flag = True
        self.saver = saver
        self.count = 0
        # Internal id
        self._id = uuid.uuid4().hex
        threading.Thread.__init__(self, name='Consumer-' + self._id)

    def __str__(self):
        return 'Consumer-' + self._id

    def run(self):
        """ Main thread function """

        while self.flag:
            url = self.queue.get()
            print(self, 'Got', url)
            self.count += 1
            if not self.saver.save(url):
                # Limit reached, break out
                print(self, 'Set limit reached, quitting')
                break

    def stop(self):
        """ Stop the thread """

        self.flag = False


if __name__ == '__main__':
    os.system('rm -f *.png')
    q = Queue(maxsize=2000)
    saver = ThumbnailImageSemaSaver(limit=25)

    producers, consumers = [], []
    for i in range(4):
        t = ThumbnailURL_Generator(q)
        producers.append(t)
        t.start()

    for i in range(3):
        t = ThumbnailURL_Consumer(q, saver)
        consumers.append(t)
        t.start()

    for t in consumers:
        t.join()
        print('Joined', t, flush=True)

    # To make sure producers dont block on a full queue
    while not q.empty():
        item = q.get()

    for t in producers:
        t.stop()
        print('Stopped', t, flush=True)

    print('Total number of PNG images', len(glob.glob('*.png')))
    os.system('rm -f *.png')
