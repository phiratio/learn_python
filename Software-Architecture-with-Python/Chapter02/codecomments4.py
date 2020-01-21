# Code listing #6

class UrlFetcher(object):
         """ Implements the steps of fetching a URL.

        Main methods:
            fetch - Fetches the URL.
            get - Return the URLs data.
        """

        def __init__(self, url, timeout=30, ntries=3, headers={}):
            """ Initializer. 
            @params
                url - URL to fetch.
                timeout - Timeout per connection (seconds).
                ntries - Max number of retries.
                headers - Optional request headers.
            """
            self.url = url
            self.timeout = timeout
            self.ntries = retries
            self.headers = headers
            # Enapsulated result object
            self.result = result 

        def fetch(self):
            """ Fetch the URL and save the result """
    
            # This loop performs a network fetch of the URL, retrying 
            # upto 'ntries' times in case of errors. 

            count, result, error = 0, None, None
            while count < self.ntries:
                try:
                    result = requests.get(self.url,
                                          timeout=self.timeout,
                                          headers = self.headers)
                except Exception as error:
                    print('Caught exception', error, 'trying again after a while')
                    # increment count
                    count += 1
                    # sleep 1 second every time
                    time.sleep(1)

            if result != None:
                # Save result
                self.result = result
    
        def get(self):
            """ Return the data for the URL """

            if self.result != None:
                return self.result.content
        
