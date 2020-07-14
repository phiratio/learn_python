# Code Listing - #3

"""

StreamHasher - Class providing hashing of data from an input stream
using pluggable algorithms

Strategy behavioral pattern:
Strategy pattern is used when we need different behaviors from a class and we should be able to configure
a class with one of many available behaviors or algorithms.
"""


class StreamHasher(object):
    """ Stream hasher class with configurable algorithm """

    def __init__(self, algorithm, chunk_size=4096):
        self.chunk_size = chunk_size
        self.hash = algorithm()

    def get_hash(self, stream):
        """ Return the hash digest """

        for chunk in iter(lambda: stream.read(self.chunk_size), ''):
            self.hash.update(chunk.encode('utf-8'))

        return self.hash.hexdigest()

    def __call__(self, stream):
        return self.get_hash(stream)


if __name__ == "__main__":
    from hashlib import md5, sha1

    # Both works
    md5h = StreamHasher(algorithm=md5)
    print(md5h(open('03-hasher-strategy-pattern.py')))
    print(StreamHasher(algorithm=sha1)(open('03-hasher-strategy-pattern.py')))
