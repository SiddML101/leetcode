class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash_map = {}

        for i in range(len(word)):
            if word[i].isupper():
                hash_map[word[i]] = 1

        count = 0

        for i in range(len(word)):
            if word[i].islower():
                if word[i].upper() in hash_map:
                    count += 1
                    hash_map.pop(word[i].upper())   

        return count