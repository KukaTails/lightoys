class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.keys = collections.deque()
        self.container = {}
        self.capacity = capacity


    def get(self, key):
        """
        :rtype: int
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.appendleft(key)
            return self.container[key]
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.appendleft(key)
            self.container[key] = value
        else:
            if len(self.keys) < self.capacity:
                self.keys.appendleft(key)
                self.container[key] = value
            else:
                old_key = self.keys.pop()
                self.container.pop(old_key)
                self.keys.appendleft(key)
                self.container[key] = value