class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def __str__(self, node=None):
        if node is None:
            node = self.node
        return self._str_recursive(node)

    def _str_recursive(self, curr):
        res = ""
        for char, child_node in curr.child.items():
            res += char
            if child_node.end:
                res += " "
            res += self._str_recursive(child_node)
        return res

    def insert_string(self, word):
        current = self.node
        for char in word:
            node = current.child.get(char)

            if node is None:
                node = TrieNode()
                current.child[char] = node
            current = node
        current.end = True

# Example usage:
my_trie = Trie()

my_trie.insert_string("app")
my_trie.insert_string("appi")
my_trie.insert_string("bappi")
my_trie.insert_string("appis")


print(my_trie)
