class Trie(object):

    def __init__(self):
        self.children = dict()

    @staticmethod
    def parse_key(s):
        if not isinstance(s, str):
            raise TypeError
        if len(s) < 1:
            raise ValueError

        s = s.strip().lower()
        return s[0], s[1:]

    def find(self, s):
        head, tail = self.parse_key(s)
        if head not in self.children:
            return None

        node = self.children[head]
        if tail:
            return node.find(tail)
        return node

    def insert(self, s):
        head, tail = self.parse_key(s)
        node = self.children.setdefault(head, Trie())
        if tail:
            node.insert(tail)
