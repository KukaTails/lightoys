class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        from collections import deque
        stack = []
        queue = deque(tokens)
        while not len(stack) == 1 or queue:
            token = queue.popleft()
            if token not in ("+", "-", "*", "/"):
                stack.append(token)
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                result = eval(str(float(lhs)) + token + str(float(rhs)))
                print(lhs + token + rhs, result)
                stack.append(str(result))
        return int(round(float(stack.pop())))
