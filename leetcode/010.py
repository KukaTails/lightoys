class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        s, p = s + "#", p + "#"
        states = set([StateNode(0, 0)])
        while states:
            new_states = set()
            for state in states:
                s_index, p_index = state.s_index, state.p_index
                if s_index == len_s and p_index == len_p:
                    return True
                if s_index == len_s or p_index == len_p:
                    if s_index == len_s and p[p_index + 1] == '*':
                        new_states.add(StateNode(s_index, p_index + 2))
                    continue
                if p[p_index + 1] != '*':
                    if p[p_index] != '.':
                        if p[p_index] == s[s_index]:
                            new_states.add(StateNode(s_index+1, p_index+1))
                        else:
                            continue
                    else:
                        new_states.add(StateNode(s_index+1, p_index+1))
                else:
                    new_states.add(StateNode(s_index, p_index+2))
                    if s_index < len_s and s[s_index] == p[p_index] or p[p_index] == '.':
                        new_states.add(StateNode(s_index+1, p_index))
                        new_states.add(StateNode(s_index+1, p_index+2))
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
              ["ab", ".*c"],
              ["ac", "ab"],
              ["ab", "a"],
              ["a", "ab"],

              # true
              ["aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*b"],
              ["ajkdkfds", "a.*"],
              ["a", "aa*"],
              ["aa", "aa*"],
              ["a", "a"],
              ["aabbc", "a.b.c"],
              ["abbbbbbc", "ab*c"],
              ["abjdfijeijc", "ab.*c"],
              ["", "a*a*"]]

for test_case in test_cases:
    print test_case, Solution().isMatch(test_case[0], test_case[1])