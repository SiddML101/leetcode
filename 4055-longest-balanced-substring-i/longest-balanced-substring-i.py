class Solution:
    def longestBalanced(self, s: str) -> int:
        max_count = 0
        for i in range (len(s)):
            hash_map = {}
            count = 0
            for j in range (i,len(s)):
                if s[j] in hash_map:
                    hash_map[s[j]] +=  1
                else:
                    hash_map[s[j]] = 1

                a = max(hash_map.values())
                all_max = all(value == a for value in hash_map.values())
                if all_max is True:
                    count = j - i + 1
                    if max_count < count:
                        max_count = count
        return max_count



