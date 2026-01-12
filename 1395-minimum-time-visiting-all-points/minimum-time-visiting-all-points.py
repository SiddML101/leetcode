class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        x_points = len(points)
        y_points = len(points[0])
        time = 0
        p1 = points[0][0]
        p2 = points[0][1]

        for i in range (1,x_points):
            a = points[i][0]
            b = points[i][1]
            c = abs(p1 - a)
            d = abs(p2 - b)
            if c <= d:
                time += c
                d = d - c
                time += d
            else:
                time += d
                c = c - d
                time += c
            p1 = a
            p2 = b

        return time
                
