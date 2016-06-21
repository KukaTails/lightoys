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
                elif s[index] in ['+', '-', '*', '/']:
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
        lhs = self.parse_term()
        while self.tokens[self.token_index] in ['+', '-']:
            op = self.tokens[self.token_index]
            self.token_index += 1
            rhs = self.parse_term()
            if op == '+':
                lhs += rhs
            else:
                lhs -= rhs
        return lhs

    def parse_term(self):
        lhs = self.parse_factor()
        while self.tokens[self.token_index] in ['*', '/']:
            op = self.tokens[self.token_index]
            self.token_index += 1
            rhs = self.parse_factor()
            if op == '*':
                lhs *= rhs
            else:
                lhs /= rhs
        return lhs

    def parse_factor(self):
        number = self.tokens[self.token_index]
        self.token_index += 1
        return int(number)

# test cases
# test_case1 = "001 + 020+20 * 50*10 / 030/10 - 5-20"
# test_case2 = "0001 / 000"
# Solution().calculate(test_case1)