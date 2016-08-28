# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes, values = [root] if root else [], []
        while nodes:
            next_level_nodes = []
            for node in nodes:
                if node:
                    values.append(node.val)
                else:
                    values.append(None)
                if not node: continue
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
            nodes = next_level_nodes if next_level_nodes.count(None) != len(next_level_nodes) else []
        print(str(values))
        return str(values)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        nodes = [val.strip() for val in data[1:-1].split(',')]
        if nodes.count('') != 0:
            nodes.remove('')
        if not nodes: return None
        index, length, root = 0, len(nodes), self.get_value(nodes[0])
        node_queue = deque([root])
        while index < length:
            node = node_queue.popleft()
            index += 1
            if index < length:
                node.left = self.get_value(nodes[index])
            else:
                break
            index += 1
            if index < length:
                node.right = self.get_value(nodes[index])
            else:
                break
            if node.left: node_queue.append(node.left)
            if node.right: node_queue.append(node.right)
        return root

    @staticmethod
    def get_value(value_str):
        value = eval(value_str)
        if value != None:
            return TreeNode(value)
        else:
            return None