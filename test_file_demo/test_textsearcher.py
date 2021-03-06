from unittest.mock import Mock, MagicMock
from unittest import TestCase
import textsearcher
import operator


class TestTextSearcher(TestCase):
    def setUp(self) -> None:
        self.db = Mock()
        self.test_data = [
            ('Python is wonderful', 0.4),
            ('I like Python', 0.8),
            ('Python is easy', 0.5),
            ('Python can be learnt in an afternoon!', 0.3),
        ]
        self.db.query = MagicMock(return_value=self.test_data)
        self.searcher = textsearcher.TextSearcher(self.db)
        self.searcher.setup(cache=True, max_items=100)

    def test_setup(self):
        self.db.connect.assert_called_with()
        self.searcher.db.configure.assert_called_with(max_items=100)
        assert len(self.test_data) == 4

    def test_search(self):
        # Mock the results data
        keyword, num = 'python', 3
        data = self.searcher.get_results(keyword, num=num)
        self.searcher.db.query.assert_called_with(keyword)

        # Verify data
        results = sorted(self.test_data, key=operator.itemgetter(1), reverse=True)[:num]
        assert data == results

    def test_result_saved_to_cache(self):
        # Mock the results data
        keyword, num = 'python', 3
        # put data to cache when you call get_results
        data = self.searcher.get_results(keyword, num=num)
        assert data == self.searcher.cache_dict[keyword]

    def test_result_taken_from_cache(self):
        # Mock the results data
        keyword, num = 'python', 3
        # put data to cache when you call get_results
        data = self.searcher.get_results(keyword, num=num)
        cache_state_snapshot = self.searcher.cache_dict.copy()
        assert data == self.searcher.cache_dict[keyword]
        # send same request, response is returned from cache
        _ = self.searcher.get_results(keyword, num=num)
        assert cache_state_snapshot == self.searcher.cache_dict
        _ = self.searcher.get_results('pokemon', num=num)
        assert cache_state_snapshot != self.searcher.cache_dict
