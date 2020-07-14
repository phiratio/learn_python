# Code Listing #1

"""
Take an input stream and hash it's contents using MD5 and return the hash digest
"""

# 01-hash_stream.py
from hashlib import md5


def hash_stream(stream, chunk_size=4096):
    """ Hash a stream of data using md5 """

    shash = md5()

    for chunk in iter(lambda: stream.read(chunk_size), ''):
        shash.update(chunk.encode('utf-8'))

    return shash.hexdigest()
# >>> import hash_stream
# >>> hash_stream.hash_stream(open('hash_stream.py'))
#     'e51e8ddf511d64aeb460ef12a43ce480'
