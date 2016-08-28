class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [ch for ch in s]
        words = self.pre_treatment(words)
        words_len = len(words)
        self.reverse(words, 0, words_len-1)

        start = end = 0
        while end <= words_len:
            if start < words_len and words[start] == ' ':
                start += 1
                end += 1
            elif end >= words_len or words[end] == ' ':
                self.reverse(words, start, end-1)
                end += 1
                start = end
            else:
                end += 1
        return "".join(words)

    @staticmethod
    def pre_treatment(words):
        # remove leading
        leading_end_pos = -1
        for ch in words:
            if ch == ' ': leading_end_pos += 1
            else: break
        words = words[leading_end_pos+1:]

        # remove trailing
        trailing_end_pos = len(words)
        for i in range(len(words)-1, -1, -1):
            if words[i] == ' ': trailing_end_pos -= 1
            else: break
        words = words[:trailing_end_pos]

        if len(words) == 0: return words
        statuses = ["InWord", "InWhiteSpace"]
        i, status = 0, statuses[0]
        while i < len(words):
            if status == statuses[0]:
                if words[i] == ' ':
                    status = statuses[1]
                i += 1
            else:
                if words[i] == ' ':
                    words.pop(i)
                else:
                    status = statuses[0]
                    i += 1
        return words

    @staticmethod
    def reverse(s, start, end):
        i, j = start, end
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


# pretreatment testing
#pre_treatment_test_cases = ["  a  b  c  ", "", " ", "  ", " a", "a ", " a ", " a b c "]
#for test_case in pre_treatment_test_cases:
#    print(Solution().pre_treatment([ch for ch in test_case]))

# reverse_word testing
reverse_word_test_cases = [" the  sky   is  blue ", "", " ", "  ", " a", "a ", " a ", "a  b  c  "]
for test_case in reverse_word_test_cases:
    print(Solution().reverseWords(test_case))