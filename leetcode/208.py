class TrieNode(object):
    def __init__(self, val):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.is_end = False
        self.next = [None] * 32

class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                node.next[index] = TrieNode(ch)
            node = node.next[index]
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")// trie.search("key");