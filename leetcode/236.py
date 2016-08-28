# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        first_path = self.find_path(root, p)
        second_path = self.find_path(root, q)
        i, length = 0, min(len(first_path), len(second_path))
        while i < length:
            if first_path[i] != second_path[i]:
                break
            i += 1
        return first_path[i - 1].val

    def find_path(self, root, node):
        self.path = []
        self.has_find = False
        self.get_path_helper(root, node)
        path = self.path
        self.path = []
        return path

    def get_path_helper(self, root, node):
        if root == None:
            return
        if root == node:
            self.path.append(root)
            self.has_find = True
            return

        if not self.has_find:
            self.path.append(root)
            self.get_path_helper(root.left, node)
            if not self.has_find: self.path.pop()

        if not self.has_find:
            self.path.append(root)
            self.get_path_helper(root.right, node)
            if not self.has_find: self.path.pop()


# testing
root = TreeNode(1)
left = TreeNode(2)
root.left = left
print(Solution().lowestCommonAncestor(root, root, left))