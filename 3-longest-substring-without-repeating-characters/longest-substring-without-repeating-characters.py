class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i = 0
        j = 0
        count = 0
        max_count = 0
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 1
                j += 1
                count += 1
            else:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                i += 1
                count -=1
            if count > max_count:
                max_count = count
        
        return max_count
            
            

        