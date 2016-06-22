class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = index = 0
        s = s.strip()
        len_s = len(s)

        while index < len_s:
            ch = s[index]
            if state == 0:
                if ch in ('+', '-'):
                    state = 1
                    index += 1
                elif ch.isdigit():
                    state = 2
                    index += 1
                elif ch == '.':
                    state = 8
                    index += 1
                else:
                    return False
            elif state == 1:
                if ch.isdigit():
                    state = 2
                    index += 1
                elif ch == '.':
                    state = 8
                    index += 1
                else:
                    return False
            elif state == 2:
                if ch.isdigit():
                    index += 1
                elif ch in ('E', 'e'):
                    state = 5
                    index += 1
                elif ch == '.':
                    state = 3
                    index += 1
                else:
                    return False
            elif state == 3:
                if ch in ('e', 'E'):
                    state = 5
                    index += 1
                elif ch.isdigit():
                    state = 4
                    index += 1
                else:
                    return False
            elif state == 4:
                if ch in ('e', 'E'):
                    state = 5
                    index += 1
                elif ch.isdigit():
                    index += 1
                else:
                    return False
            elif state == 5:
                if ch.isdigit():
                    state = 7
                    index += 1
                elif ch in ('+', '-'):
                    state = 6
                    index += 1
                else:
                    return False
            elif state == 6:
                if ch.isdigit():
                    state = 7
                    index += 1
                else:
                    return False
            elif state == 7:
                if ch.isdigit():
                    index += 1
                else:
                    return False
            elif state == 8:
                if ch.isdigit():
                    state = 9
                    index += 1
                else:
                    return False
            elif state == 9:
                if ch.isdigit():
                    index += 1
                elif ch in ('E', 'e'):
                    state = 5
                    index += 1
                else:
                    return False

        if state in (2, 3, 4, 7, 9):
            return True
        else:
            return False

# test cases
test_cases = [
    # True
    " -.8",
    "3",
    " 3 ",
    "+1",
    "-2",
    "020",
    "00020",
    "-1.1",
    "1.1",
    ".1",
    ".1E-10",
    ".1e10",
    "1.",
    "1.E10",
    "-1.e-10",
    "0E0",
    "0e0",
    "1e-1",
    "999999999999999999999999999999999999999999999",
    "-9999999999999999999999999999999999999999999999",
    "99999999999999999999999999999999999999999999.99999999999999999999999999999999999999999999999",
    "-999999999999999999999999999999999999999999999999.99999999999999999999999999999999999999999999",

    # False
    "0x4",
    "1.0f",
    " . ",
    " + .8",
    " + 1 ",
    " - 2 "
]

for test_case in test_cases:
    Solution().isNumber(test_case)