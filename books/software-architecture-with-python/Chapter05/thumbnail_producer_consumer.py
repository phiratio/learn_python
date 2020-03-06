# Code Listing #2

"""

Thumbnail converter using producer-consumer architecture:
1. Producers are a specialized class of workers (threads) producing the data. They may receive the data from a specific
source(s), or generate the data themselves.
2. Producers add the data to a shared synchronized queue. In Python, this queue is provided by the Queue class in the
aptly named queue module.
3. Another set of specialized class of workers, namely consumers, wait on the queue to get (consume) the data.
Once they get the data, they process it and produce the results.
4. The program comes to an end when the producers stop generating data and the consumers are starved of data.
Techniques like timeouts, polling, or poison pills can be used to achieve this.
When this happens, all threads exit, and the program completes.
"""

import threading
import time
import string
import random
import urllib.request

from PIL import Image
from queue import Queue


class ThumbnailURL_Generator(threading.Thread):
    """ Worker class that generates image URLs """

    def __init__(self, queue, sleep_time=1, ):
        self.sleep_time = sleep_time
        self.queue = queue
        # A flag for stopping
        self.flag = True
        # sizes
        self._sizes = (240, 320, 360, 480, 600, 720)
        # URL scheme
        self.url_template = 'https://dummyimage.com/%s/%s/%s.jpg'
        threading.Thread.__init__(self, name='url producer')

    def __str__(self):
        return 'Producer'

    def get_size(self):
        return '%dx%d' % (random.choice(self._sizes),
                          random.choice(self._sizes))

    def get_color(self):
        return ''.join(random.sample(string.hexdigits[:-6], 3))

    # We start a thread using its start method, though the overridden method in the Thread subclass is run.
    # This is because, in the parent Thread class, the start method sets up some state,
    # and then calls the run method internally. This is the right way to call the thread's run method.
    # It should never be called directly.
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


class ThumbnailURL_Consumer(threading.Thread):
    """ Worker class that consumes URLs and generates thumbnails """

    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        threading.Thread.__init__(self, name='consumer')

    def __str__(self):
        return 'Consumer'

    def thumb_image(self, url, size=(64, 64), format='.png'):
        """ Save image thumbnails, given a URL """

        im = Image.open(urllib.request.urlopen(url))
        # filename is last part of URL minus extension + '.format'
        filename = url.split('/')[-1].split('.')[0] + '_thumb' + format
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(filename)
        print(self, 'Saved', filename)

    def run(self):
        """ Main thread function """

        while self.flag:
            url = self.queue.get()
            print(self, 'Got', url)
            self.thumb_image(url)

    def stop(self):
        """ Stop the thread """

        self.flag = False
        self.join()


if __name__ == '__main__':

    q = Queue(maxsize=200)
    producers, consumers = [], []
    for i in range(2):
        t = ThumbnailURL_Generator(q)
        producers.append(t)
        t.start()

    for i in range(2):
        t = ThumbnailURL_Consumer(q)
        consumers.append(t)
        t.start()
