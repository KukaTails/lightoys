# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList
        self.stack = []
        self.stack.append([nestedList, 0])



    def next(self):
        """
        :rtype: int
        """
        elem, index = self.stack.pop()
        if elem.isInteger():

            return elem
        else:
            while len(self.stack) != 0:
                while not elem[index].isInteger():
                    self.stack.append([elem, index])
                    elem, index = elem[index], 0
                if index < len(elem)-1:
                    self.stack.append([elem, index+1])
                    return elem[index]
                else:
                    elem, index = self.stack.pop()
                    index += 1

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        element, index = self.stack[-1]
        if element.isInteger():
            return True
        else:
            if index >= len(element):
                return False
            else:
                return True



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())