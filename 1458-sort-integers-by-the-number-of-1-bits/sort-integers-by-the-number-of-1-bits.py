class Solution:
    def sortByBits(self, arr):
        hash_map = {}

        for i in range(len(arr)):
            a = bin(arr[i])[2:]
            count = 0
            for j in range(len(a)):
                if a[j] == '1':
                    count += 1
            hash_map[arr[i]] = count

        arr = sorted(arr, key=lambda x: (hash_map[x], x))
        return arr