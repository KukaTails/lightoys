class Node(object):
    def __init__(self, value=None):
        self.val = value
        self.next = [None] * 26
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                node.next[index] = Node(ch)
            node = node.next[index]
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = [self.root]
        for ch in word:
            new_nodes = []
            for node in nodes:
                if ch == '.':
                    for x in node.next:
                        if x:
                            new_nodes.append(x)
                else:
                    index = ord(ch) - ord('a')
                    if node.next[index]:
                        new_nodes.append(node.next[index])
            nodes = new_nodes
        is_find = False
        for node in nodes:
            if node.is_end:
                is_find = True
                break
        return is_find

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
