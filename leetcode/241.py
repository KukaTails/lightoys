class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input)

    def helper(self, exp):
        has_operator, result = False, []
        for i, ch in enumerate(exp):
            if ch in ("+", "-", "*"):
                l_values = self.helper(exp[:i])
                r_values = self.helper(exp[i+1:])
                for i in l_values:
                    for j in r_values:
                        result.append(eval(str(i) + ch + str(j)))
                has_operator = True
        return result if has_operator else [int(exp)]
