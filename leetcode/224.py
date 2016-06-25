class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.tokens = self.scan(s + " ")
        self.tokens.append("#")
        self.token_index = 0
        return self.parse_exp()

    def scan(self, s):
        state = 0
        index = 0
        len_s = len(s)
        last_index = 0
        tokens = []
        while index < len_s:
            if state == 0:
                if '0' <= s[index] <= '9':
                    state = 1
                    index += 1
                elif s[index] in ['+', '-', '(', ')']:
                    state = 2
                    index += 1
                else:
                    last_index += 1
                    index += 1
            elif state == 1:
                if '0' <= s[index] <= '9':
                    state = 1
                    index += 1
                else:
                    state = 2
            if state == 2:
                state = 0
                tokens.append(s[last_index:index])
                last_index = index
        return tokens

    def parse_exp(self):
        lhs = self.parse_factor()
        while self.tokens[self.token_index] in ['+', '-']:
            op = self.tokens[self.token_index]
            self.token_index += 1
            rhs = self.parse_factor()
            if op == '+':
                lhs += rhs
            else:
                lhs -= rhs
        return lhs

    def parse_factor(self):
        if self.tokens[self.token_index] == '(':
            self.token_index += 1
            value = self.parse_exp()
            self.token_index += 1
        else:
            value = self.tokens[self.token_index]
            self.token_index += 1
        return int(value)

# test cases
# test_case1 = "001 + 020+20 * 50*10 / 030/10 - 5-20"
# test_case2 = "0001 / 000"
# test_case3 = "0"
# test_case4 = "(1+(4+5+2)-3)+(6+8)"
# test_case5 = "1 + 1"
# test_case6 = "2-(5-6)"

# Solution().calculate(test_case1)