class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack2) > 0:
            self.stack2.pop()
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1[len(self.stack1)-1])
                self.stack1.pop()
            self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2[len(self.stack2)-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1[len(self.stack1)-1])
                self.stack1.pop()
            return self.stack2[len(self.stack2)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

# testing
queue = Queue()
queue.push(1)
print(queue.peek())
queue.pop()
print(queue.empty())
