# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        k, heap, answer = len(lists), [], []

        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, lists[i]])
        while heap:
            min_nodes = heapq.heappop(heap)
            answer.append(min_nodes[0])
            if min_nodes[1].next:
                heapq.heappush(heap, [min_nodes[1].next.val, min_nodes[1].next])
        return answer
