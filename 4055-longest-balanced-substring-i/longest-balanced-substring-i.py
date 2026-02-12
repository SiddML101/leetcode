class Solution:
    def longestBalanced(self, s: str) -> int:
        max_count = 0

        for i in range(len(s)):
            hash_map = {}
            max_freq = 0

            for j in range(i, len(s)):
                if s[j] in hash_map:
                    hash_map[s[j]] += 1
                else:
                    hash_map[s[j]] = 1

                if hash_map[s[j]] > max_freq:
                    max_freq = hash_map[s[j]]

                distinct = len(hash_map)
                length = j - i + 1

                if max_freq * distinct == length:
                    if max_count < length:
                        max_count = length

        return max_count
