class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        exist_state = []
        s, p = s + "#", p + "#"
        states = set([StateNode(0, 0)])
        while states:
            new_states = set()
            for state in states:
                s_index, p_index = state.s_index, state.p_index
                if s_index == len_s and p_index == len_p:
                    return True
                if s_index == len_s or p_index == len_p:
                    if s_index == len_s and p[p_index] == '*':
                        if StateNode(s_index, p_index+1) not in exist_state:
                            new_states.add(StateNode(s_index, p_index+1))
                            exist_state.add(StateNode(s_index, p_index+1))
                    continue
                if p[p_index] == '?':
                    if StateNode(s_index+1, p_index+1) not in exist_state:
                        new_states.add(StateNode(s_index+1, p_index+1))
                        exist_state.add(StateNode(s_index+1, p_index+1))
                elif p[p_index] == '*':
                    if StateNode(s_index, p_index+1) not in exist_state:
                        new_states.add(StateNode(s_index, p_index+1))
                        exist_state.add(StateNode(s_index, p_index+1))
                    if s_index < len_s:
                        if StateNode(s_index+1, p_index) not in exist_state:
                            new_states.add(StateNode(s_index+1, p_index))
                            exist_state.add(StateNode(s_index+1, p_index))
                        if StateNode(s_index+1, p_index) not in exist_state:
                            new_states.add(StateNode(s_index+1, p_index+1))
                            exist_state.add(StateNode(s_index+1, p_index+1))
                else:
                    if p[p_index] == s[s_index]:
                        if StateNode(s_index+1, p_index+1) not in exist_state:
                            new_states.add(StateNode(s_index+1, p_index+1))
                            exist_state.add(StateNode(s_index+1, p_index+1))
            states = new_states
        return False

class StateNode(object):
    def __init__(self, str_index, pattern_index):
        self.s_index = str_index
        self.p_index = pattern_index

    def __eq__(self, other):
        if isinstance(other, StateNode):
            return self.s_index == other.s_index and self.p_index == other.p_index
        else:
            return False

    def __repr__(self):
        return "StateNode({}, {})".format(self.s_index, self.p_index)

    def __hash__(self):
        return hash(self.__repr__())

# test cases
test_cases = [
              #false
              ["aa", "a"],
              ["aaa", "aab"],
              ["aab", "c*a*b"],

              # true
              ["abbbaaababbaaabaaabbbabbbbaaabbaaababaabbbbbbaababbabababbababaaabbbbbabababaababaaaaaaabbbaabaabbbaabba"
               "baababbabaababbbabbaaabbbaaaababbaaabbaabaabbbbbaaababaabaabaaabbabaabbbabbbaabbababaabbbbbbbbaaa",
               "*ba***bba*b**abbaa***a*****b*a*bb*b***a*bbb***a***bba*****a****a*a*b**aaaba*aab*a*aa***a*a*b**b**a*b*"],
              ["abababbbbabbbbbaabaabaabbbababbababbbabaaababaabbbbbbbabaaabaabbababbbbaaaabbabababbaaaaaabaabbaaabbbabb"
               "bbbaaaabaaaaaabababbbaababbaaabbaabaabbbbabbaaabbbbabbaaabaabbbbaabaabbbbbbbbbbaaabbbbbbababbbbbaab",
               "a*bba**abbba*bb*aa***ab*bbaa*b**aaab**baa*aa*b**bb**ba**b**aa**a**bb**b*ab*******b*bba******aba*ab**a"],
              ["", "*"],
              ["abcdefg", "*"],
              ["aaaaaabaaaaaaab", "a*b*b"],
              ["ab", "ab"],
              ["abc", "a??"],
              ["aa", "aa*"],
              ["a", "*a"],
              ["aabbc", "a?b?c"],
              ["abbbbbbc", "a*bc"],
              ["abjdfijeijc", "ab?*c"]]

for test_case in test_cases:
    print test_case, Solution().isMatch(test_case[0], test_case[1])