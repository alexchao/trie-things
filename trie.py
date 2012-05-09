def normalize_key(s):
    if not isinstance(s, str):
        raise TypeError
    if len(s) < 1:
        raise ValueError

    s = s.strip().lower()
    return s, s[0], s[1:]


class Trie(object):

    def __init__(self):
        self.children = dict()

    def find(self, s):
        _, head, tail = normalize_key(s)
        if head not in self.children:
            return None

        node = self.children[head]
        if tail:
            return node.find(tail)
        return node

    def insert(self, s):
        _, head, tail = normalize_key(s)
        node = self.children.setdefault(head, Trie())
        if tail:
            node.insert(tail)
