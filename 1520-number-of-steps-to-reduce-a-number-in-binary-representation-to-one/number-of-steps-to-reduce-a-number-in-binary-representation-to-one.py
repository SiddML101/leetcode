class Solution:
    def numSteps(self, s: str) -> int:
        a = int(s,2)
        count = 0
        b = a

        for i in range (b):
            if a == 1:
                break
            if a % 2 == 0:
                a = a // 2
                count += 1
            else:
                a += 1
                count += 1
        return count
