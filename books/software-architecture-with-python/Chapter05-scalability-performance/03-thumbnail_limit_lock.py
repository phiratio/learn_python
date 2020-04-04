# Code Listing #3

"""

Thumbnail producer/consumer - Limiting number of images using a lock

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


class ThumbnailImageSaver(object):
    """ Class which saves URLs to thumbnail images and keeps a counter """

    def __init__(self, limit=10):
        self.limit = limit
        self.lock = threading.Lock()
        # Since the images are randomly generated, there is a minor chance of one image URL being same
        # as another one created previously, causing the filenames to clash.
        # Using a dictionary takes care of such possible duplicates.
        self.counter = {}

    def thumbnail_image(self, url, size=(64, 64), format='.png'):
        """ Save image thumbnails, given a URL """

        im = Image.open(urllib.request.urlopen(url))
        # filename is last two parts of URL minus extension + '.format'
        pieces = url.split('/')
        filename = ''.join((pieces[-2], '_', pieces[-1].split('.')[0], '_thumb', format))
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(filename)
        print('Saved', filename)
        self.counter[filename] = 1
        return True

    def save(self, url):
        """ Save a URL as thumbnail """

        with self.lock:
            if len(self.counter) >= self.limit:
                return False
            self.thumbnail_image(url)
            print('\tCount=>', len(self.counter))
            return True


class ThumbnailURL_Consumer(threading.Thread):
    """ Worker class that consumes URLs and generates thumbnails """

    def __init__(self, queue, saver):
        self.queue = queue
        self.flag = True
        self.saver = saver
        self.count = 0
        # Internal id
        self._id = uuid.uuid4().hex
        threading.Thread.__init__(self, name=f'Consumer-{self._id}')

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
                self.stop()
                break

    def stop(self):
        """ Stop the thread """

        self.flag = False


if __name__ == '__main__':
    os.system('rm -f *.png')
    q = Queue(maxsize=2000)
    saver = ThumbnailImageSaver(limit=40)

    producers, consumers = [], []
    for i in range(4):
        t = ThumbnailURL_Generator(q)
        producers.append(t)
        t.start()

    for i in range(3):
        t = ThumbnailURL_Consumer(q, saver)
        consumers.append(t)
        t.start()

    # main thread doesn't call stop, but join on them.
    # This is because the consumers exit automatically when the limit is reached,
    # so the main thread should just wait for them to stop.
    for t in consumers:
        t.join()
        print('Joined', t, flush=True)

    # To make sure producers dont block on a full queue
    while not q.empty():
        print('GRAB ITEM FOR NOTHING')
        item = q.get()

    # We stop the producers after the consumers exit—explicitly so—since they would otherwise keep working forever,
    # since there is no condition for the producers to exit.
    for t in producers:
        t.stop()
        print('Stopped', t, flush=True)

    print('Total number of PNG images', len(glob.glob('*.png')))
