import operator


class TextSearcher:
    """A class which performs a text search and returns results"""

    def __init__(self, db):
        super().__init__()
        self.cache = False
        self.cache_dict = {}
        self.db = db
        self.db.connect()

    def setup(self, cache=False, max_items=500):
        """Setup parameters such as caching"""
        self.cache = cache
        # call configure to the db
        self.db.configure(max_items=max_items)

    def get_results(self, keyword, num=10):
        """Query keyword on db and get results for given keyword"""

        # If results in cache return from there
        if keyword in self.cache_dict:
            print('From cache')
            return self.cache_dict[keyword]

        results = self.db.query(keyword)
        # Results are list of (string, weight's) tuples
        results = sorted(results, key=operator.itemgetter(1), reverse=True)[:num]
        # Cache it
        if self.cache:
            self.cache_dict[keyword] = results

        return results
