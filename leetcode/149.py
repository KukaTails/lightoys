# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Seg(object):
    def __init__(self, lhs, rhs):
        if lhs.x <= rhs.x:
            self.lhs, self.rhs = lhs, rhs
        else:
            self.lhs, self.rhs = rhs, lhs

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        str = "Segment<{},{}><{},{}>".format(self.lhs.x, self.lhs.y, self.rhs.x, self.rhs.y)
        return hash(str)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        hash_table = {}
        size = len(points)
        if size <= 2:
            return size
        max_cnt = 0
        for i in xrange(size):
            for j in xrange(i+1, size):
                lhs, rhs = points[i], points[j]
                if Seg(lhs, rhs) in hash_table.keys():
                    cnt = hash_table[Seg(lhs, rhs)]
                    max_cnt = cnt if cnt > max_cnt else max_cnt
                    continue
                normal = [-(rhs.y - lhs.y), rhs.x - lhs.x]
                cnt, segments = 0, []
                for k in xrange(size):
                    if normal[0] == 0 and normal[1] == 0:
                        if lhs.x == points[k].x and rhs.y == points[k].y:
                            cnt += 1
                            segments.append(Seg(lhs, points[k]))
                    elif points[k].x == lhs.x and points[k].y == lhs.y:
                        cnt += 1
                        segments.append(Seg(lhs, points[k]))
                    elif normal[0] * (points[k].x - lhs.x) + normal[1] * (points[k].y - lhs.y) == 0:
                        cnt += 1
                        segments.append(Seg(lhs, points[k]))
                for segment in segments:
                    hash_table[segment] = cnt
                max_cnt = cnt if cnt > max_cnt else max_cnt
        return max_cnt

# testing
test_cases = [[],
              [[0, 0]],
              [[0, 0], [1, 1]],
              [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]],
              [[0, 0], [0, 0], [0, 0]]]

for test_case in test_cases:
    points = []
    for point in test_case:
        points.append(Point(point[0], point[1]))
    print(Solution().maxPoints(points))
