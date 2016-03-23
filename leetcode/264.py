class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        heap, ans, count, poped = [], [], 1, 0
        heapq.heappush(heap, 1)
        while count <= n:
            x = heapq.heappop(heap)
            poped += 1
            ans.append(x)
            for i in (2, 3, 5):
                heapq.heappush(heap, i * x)
            count += 3
        while heap and poped < n:
            heapq.heappop(heap)
            poped += 1
        return heap[0]
