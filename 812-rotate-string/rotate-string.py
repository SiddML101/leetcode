class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        arr1 = list(s)
        arr2 = list(goal)
        flag = False
        m_count = 0
        for i in range (len(s)):
            count = 0
            for j in range (len(s)):
                if arr1[j] == arr2[j]:
                    count += 1
                else:
                    break
            if count > m_count:
                m_count = count
            b = arr1[0]
            arr1.append(b)
            arr1.pop(0)
            if m_count == len(s):
                return True
           
        
        return False
        