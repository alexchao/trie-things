import unittest

from trie import Trie

class TrieTest(unittest.TestCase):

    def test_empty_trie(self):
        t = Trie()

    def test_find(self):
        t = Trie().find('foo')
        assert t == None

    def test_insert(self):
        t = Trie()
        t.insert('foo')
        assert t.find('foo')

if __name__ == '__main__':
    unittest.main()
