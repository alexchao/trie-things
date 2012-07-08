import unittest

from trie import Trie


class ParseKeyTest(unittest.TestCase):

    def test_accepts_strings_only(self):
        try:
            h, t = Trie.parse_key(5)
            assert False, 'Expected error for non-string key'
        except TypeError:
            pass

    def test_empty_string(self):
        h, t = Trie.parse_key('')
        assert h == ''
        assert t == ''

    def test_one_character(self):
        h, t = Trie.parse_key('a')
        assert h == 'a'
        assert t == ''


class TrieTest(unittest.TestCase):

    def test_empty_trie(self):
        Trie()

    def test_finds_nodes(self):
        t1, t2, t3, t4 = Trie(), Trie(), Trie(), Trie()
        t1.children['b'] = t2
        t2.children['a'] = t3
        t3.children['r'] = t4
        trie = t1.find('bar')
        assert trie == t4

    def test_finds_nothing(self):
        t = Trie().find('foo')
        assert t == None

    def test_inserts(self):
        t = Trie()
        t.insert('foo')
        assert t.find('foo')


if __name__ == '__main__':
    unittest.main()
