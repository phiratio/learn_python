# coding=utf-8

# Code Listing #12
"""

Example of using bloom filter

NOTE: This works only with Python2.x So when should we use a bloom filter as opposed to, say, a dictionary or set in
Python? Here are some general principles and real-world usage scenarios:

When you are fine with not storing the actual element itself but only interested in the presence (or absence) of the
element. In other words, where your application use case relies more on checking the absence of data than its
presence. When the size of your input data is so large that storing each and every item in a deterministic data
structure (as a dictionary or hashtable) in memory is not feasible. A bloom filter takes much less data in memory as
opposed to a deterministic data structure. When you are fine with a certain well-defined error rate of false
positives with your dataset – let us say this is 5% out of 1 million pieces of data – you can configure a bloom
filter for this specific error rate and get a data hit rate that will satisfy your requirements. Some real-world
examples of using bloom filters are as follows:

Security testing: Storing data for malicious URLs in browsers, for example
Bio-informatics: Testing the presence of a certain pattern (a k-mer) in a genome
To avoid storing URLs with just one hit in a distributed web caching infrastructure
"""

from pybloom import BloomFilter
import requests


# Uncomment for profiling with line profiler or memory profiler

# @profile
def hound():
    f = BloomFilter(capacity=100000, error_rate=0.01)
    text = requests.get('https://www.gutenberg.org/files/2852/2852-0.txt').text

    for word in text.split():
        word = word.lower().strip()
        f.add(word)

    print len(f)
    print len(text.split())

    for w in ('holmes', 'watson', 'hound', 'moor', 'queen'):
        print 'Found', w, w in f


if __name__ == "__main__":
    hound()
