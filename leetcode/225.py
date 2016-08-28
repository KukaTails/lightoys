class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            self.queue1.append(x)
        elif len(self.queue1) > 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.queue1) > 0:
            while len(self.queue1) > 1:
                val = self.queue1.popleft()
                self.queue2.append(val)
            self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                val = self.queue2.popleft()
                self.queue1.append(val)
            self.queue2.popleft()

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue1) > 0:
            while len(self.queue1) > 1:
                val = self.queue1.popleft()
                self.queue2.append(val)
            result = self.queue1.popleft()
            self.queue2.append(result)
            return result
        else:
            while len(self.queue2) > 1:
                val = self.queue2.popleft()
                self.queue1.append(val)
            result = self.queue2.popleft()
            self.queue1.append(result)
            return result

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0

# testing
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.top())
stack.pop()
print(stack.top())
print(stack.empty())
stack.pop()
print(stack.empty())