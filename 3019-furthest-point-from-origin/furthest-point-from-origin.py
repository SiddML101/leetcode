class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        countL = 0
        countR = 0
        for i in range (len(moves)):
            if moves[i] == 'L':
                countL += 1
            if moves[i] == 'R':
                countR += 1
        count = 0
        if countL > countR:
            for i in range (len(moves)):
                if moves[i] == 'L' or moves[i] == "_":
                    count += 1
                if moves[i] == 'R':
                    count -= 1
            return count

        else:
            for i in range (len(moves)):
                if moves[i] == 'R' or moves[i] == "_":
                    count += 1
                else:
                    count -= 1
            return count

        