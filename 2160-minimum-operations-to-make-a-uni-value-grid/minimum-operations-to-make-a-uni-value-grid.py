class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = len(grid)
        b = len(grid[0])

        arr = []

        for i in range (a):
            for j in range (b):
                arr.append(grid[i][j])


        arr.sort()
        n = len(arr)//2
        m = arr[n]
        count = 0
        for i in range (len(arr)):
            diff = abs(m-arr[i])
            if diff % x == 0:
                count += diff/x
            else:
                return -1

        return int(count)

        
        