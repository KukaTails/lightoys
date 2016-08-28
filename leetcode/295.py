class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 0
        self.root = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.cnt += 1
        self.root = self.insert(self.root, Node(num))

    def insert(self, root, Node):
        if not root:
            return Node
        if Node.value < root.value:
            root.left = self.insert(root.left, Node)
        else:
            root.right = self.insert(root.right, Node)
        root.maintain()
        return root

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        middle = self.cnt // 2
        if self.cnt % 2 == 0:
            return (self.findKth(self.root, middle) + self.findKth(self.root, middle + 1)) / 2.0
        else:
            return self.findKth(self.root, middle + 1)

    def findKth(self, root, k):
        l_size = 0 if not root.left else root.left.size
        if l_size + 1 == k:
            return root.value
        elif l_size >= k:
            return self.findKth(root.left, k)
        else:
            return self.findKth(root.right, k - 1 - l_size)

class Node:
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.left = None
        self.right = None

    def maintain(self):
        size = 1
        if self.left: size += self.left.size
        if self.right: size += self.right.size
        self.size = size

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

# testing
mf = MedianFinder()
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
#mf.addNum(2)
#mf.addNum(4)
print(mf.findMedian())