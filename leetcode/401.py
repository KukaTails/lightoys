class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.hours = []
        self.minutes = []
        result = []
        for i in range(num+1):
            tmp_hours = self.getHours(i)
            tmp_minutes = self.getMinutes(num-i)
            for hour in tmp_hours:
                for minute in tmp_minutes:
                    str_minute = str(minute) if len(str(minute)) == 2 else '0' + str(minute)
                    time = str(hour) + ':' + str_minute
                    result.append(time)
        return result

    def getHours(self, num):
        MAX_HOURS = 11
        result = []
        if num == 0:
            return [0]
        self.getSets([], 0, 0, [8, 4, 2, 1], 4, num, result)
        return self.reduce_and_filter(result, MAX_HOURS)

    def getMinutes(self, num):
        MAX_MINUTES = 59
        result = []
        if num == 0:
            return [0]
        self.getSets([], 0, 0, [32, 16, 8, 4, 2, 1], 6, num, result)
        return self.reduce_and_filter(result, MAX_MINUTES)

    def reduce_and_filter(self, sets, MAX_VALUE):
        from functools import reduce
        ans = []
        for set in sets:
            sum = reduce(lambda x, y: x+y, set, 0)
            if sum <= MAX_VALUE:
                ans.append(sum)
        return ans



    def getSets(self, ans, index, cnt, sets, length, nums, ans_sets):
        import copy
        if index >= length or cnt >= nums:
            if cnt == nums:
                ans_sets.append(copy.deepcopy(ans))
            return
        self.getSets(ans, index+1, cnt, sets, length, nums, ans_sets)
        ans.append(sets[index])
        self.getSets(ans, index+1, cnt+1, sets, length, nums, ans_sets)
        ans.pop()

# testing
result = Solution().readBinaryWatch(1)
print(result)
