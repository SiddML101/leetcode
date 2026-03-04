class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        count = 0

        for i in range (rows):
            for j in range (cols):

                if mat[i][j] == 1:
                    row_count = 0
                    col_count = 0


                    for k in range (cols):
                        if mat[i][k] == 1:
                            row_count += 1

                    for k in range (rows):
                        if mat[k][j] == 1:
                            col_count += 1
                    

                    if row_count == 1 and col_count == 1:
                        count += 1
        return count
        
            

        