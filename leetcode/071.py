class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        string = ""
        for ch in path + "/":
            if ch == "/":
                if string == ".":
                    pass
                elif string == "..":
                    if stack: stack.pop()
                elif string:
                    stack.append(string)
                string = ""
            else:
                string += ch
        return "/" + "/".join(stack)
