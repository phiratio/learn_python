# Code Listing #5

"""

A simple web client using Twisted

"""

# twisted_fetch_url.py
import sys
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers


def save_page(page, filename='content.html'):
    open(filename, 'w').write(page)


def handle_error(error):
    print(error)


def finish_processing(value):
    print("Shutting down...")
    reactor.stop()


if __name__ == "__main__":
    agent = Agent(reactor)
    url = sys.argv[1] if len(sys.argv) >= 2 else b'http://info.cern.ch/'
    deferred = agent.request(
        b'GET',
        url,
        Headers({'User-Agent': ['Twisted Web Client Example']}),
        None
    )
    deferred.addCallbacks(save_page, handle_error)
    deferred.addBoth(finish_processing)
    reactor.run()
