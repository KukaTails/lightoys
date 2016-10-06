class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        length = len(matrix)
        heap, record = [], [0] * length
        for i in range(length):
            heapq.heappush(heap, [matrix[i][record[i]], i])
            record[i] += 1

        count = 1
        while count < k:
            item = heapq.heappop(heap)
            arr_index = item[1]
            if record[arr_index] < length:
                heapq.heappush(heap, [matrix[arr_index][record[arr_index]], arr_index])
                record[arr_index] += 1
            count += 1
        return heapq.heappop(heap)[0]


# testing
test_cases = [([[1,5,9],[10,11,13],[12,13,15]], 8)]
results = [13]
for i, test_case in enumerate(test_cases):
    assert results[i] == Solution().kthSmallest(test_case[0], test_case[1])
