class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash_mapa = {}
        hash_mapb = {}
        arr = []

        for i in range(len(A)):

            hash_mapa[A[i]] = 1
            hash_mapb[B[i]] = 1

            count = 0

            for key in hash_mapa:
                if key in hash_mapb:
                    count += 1

            arr.append(count)

        return arr