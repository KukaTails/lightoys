# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        left_inorder, right_inorder = inorder[:root_index], inorder[root_index+1:]
        left_len, right_len = len(left_inorder), len(right_inorder)
        left_post, right_post = inorder[:left_len], inorder[left_len:left_len+right_len]
        root.left = self.buildTree(left_inorder, left_post)
        root.right = self.buildTree(right_inorder, right_post)
        return root
