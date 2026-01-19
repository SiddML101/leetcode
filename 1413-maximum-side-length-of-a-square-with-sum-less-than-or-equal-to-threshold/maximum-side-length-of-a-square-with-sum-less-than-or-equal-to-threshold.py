from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        s = min(rows, cols)

        # Prefix sum matrix
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        
        for size in range(s, 0, -1):
            for r in range(rows - size + 1):
                for c in range(cols - size + 1):
                    square_sum = (
                        prefix[r + size][c + size]
                        - prefix[r][c + size]
                        - prefix[r + size][c]
                        + prefix[r][c]
                    )
                    if square_sum <= threshold:
                        return size

        return 0
