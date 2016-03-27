class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_chars = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        pre_set = [""]
        for ch in digits:
            cur_set = []
            for element in pre_set:
                for append_ch in num_to_chars[int(ch)]:
                    cur_set.append(element + append_ch)
            pre_set = cur_set
        return pre_set if digits != "" else []
