class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment = 0
        flag = False
        for i in range (len(s)):
            if s[i] == '1' and flag == False:
                continue
            if s[i] == '0' and flag == False:
                flag = True
            if s[i] == '1' and flag == True:
                return False

        return True
