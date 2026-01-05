class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        arr = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] <= 0:
                    count += 1

        sum = 0

        # even negatives → all abs
        if count % 2 == 0:
            for i in range(rows):
                for j in range(cols):
                    sum += abs(matrix[i][j])
            return sum

        # odd negatives (includes count == 1)
        min_abs = float('inf')
        for i in range(rows):
            for j in range(cols):
                sum += abs(matrix[i][j])
                if abs(matrix[i][j]) < min_abs:
                    min_abs = abs(matrix[i][j])

        sum -= 2 * min_abs
        return sum
