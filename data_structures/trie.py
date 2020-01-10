# Implement an autocomplete system.
# That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

# nop -> 0(N)
def match_prefix(s, l):
    results = set()
    l = set(l)
    for word in l:
        if word.startswith(s):
            results.add(word)
    return results


s = 'de'
l = ['dog', 'deer', 'deal']
match_prefix(s, l)


# yup
class Trie:

    def __init__(self):
        self._trie = {}

    def insert(self, word):
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['*'] = True  # idicates completion of word
        print(self._trie)

    def elements(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        print('hop')
        print(trie)
        return self._element(trie)

    def _element(self, b):
        results = []
        for s, v in b.items():
            if s == '*':
                subresult = ['']
            else:
                subresult = [s + k for k in self._element(v)]
            results.append(subresult[0])
        return results


s = 'de'
words = ['dog', 'deer', 'deal', 'dear']
trie = Trie()
for word in words:
    trie.insert(word)


def match_prefix(s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]


match_prefix(s)
