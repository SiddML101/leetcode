class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

            
        hashmap1 = dict(sorted(hashmap.items(), key=lambda item:item[1], reverse = True))
        
        arr = []
        arr = list(hashmap1.keys())[:k]

        return arr
