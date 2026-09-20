class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r = len(board)
        c = len(board[0])

        for i in range (r):
            hashmap1 = {}
            for j in range (c):
                if board[i][j] not in hashmap1 and board[i][j] != ".":
                    hashmap1[board[i][j]] = 1
                elif board[i][j] in hashmap1:
                    return False
                
        for i in range (c):
            hashmap1 = {}
            for j in range (r): 
                if board[j][i] not in hashmap1 and board[j][i] != ".":
                    hashmap1[board[j][i]] = 1
                elif board[j][i] in hashmap1:
                    return False

        for i in range (0,9,3):
            for j in range (0,9,3):
                hashmap1 = {}    

                for x in range (i,i+3):
                    for y in range (j,j+3):
                        if board[x][y] not in hashmap1 and board[x][y] != ".":
                            hashmap1[board[x][y]] = 1
                        elif board[x][y] in hashmap1:
                            return False


        return True
                

        