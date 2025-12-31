class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                sum_left_diagonal = 0
                sum_right_diagonal = 0
                block = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        block.append(grid[r][c])

                        if (r - i) == (c - j):
                            sum_left_diagonal += grid[r][c]
                        if (r - i) + (c - j) == 2:
                            sum_right_diagonal += grid[r][c]

                if set(block) != set(range(1, 10)):
                    continue

                row_sums = []
                col_sums = []

                for x in range(3):
                    row_sums.append(sum(grid[i + x][j:j + 3]))
                    col_sums.append(sum(grid[i + r][j + x] for r in range(3)))

                all_sums = row_sums + col_sums + [sum_left_diagonal, sum_right_diagonal]

                if len(set(all_sums)) == 1:
                    count += 1

        return count
