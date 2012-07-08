class Trie(object):

    def __init__(self):
        self.children = dict()

    @staticmethod
    def parse_key(s):
        """Break key into its constituent parts.

        Return tuple of <head character>, <tail string>
        """
        if not isinstance(s, str):
            raise TypeError('Key must be a string')

        s = s.strip().lower()
        if s == '':
            return '', ''
        return s[0], s[1:]

    def find(self, s):
        node = self
        head, tail = self.parse_key(s)
        while head != '':
            if head not in node.children:
                return None
            node = node.children[head]
            head, tail = self.parse_key(tail)

        return node

    def insert(self, s):
        head, tail = self.parse_key(s)
        node = self.children.setdefault(head, Trie())
        if tail:
            node.insert(tail)
