class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        seen = {}
        count = 0
        arr = []

        for i in range(len(A)):

            seen[A[i]] = seen.get(A[i], 0) + 1
            if seen[A[i]] == 2:
                count += 1

            seen[B[i]] = seen.get(B[i], 0) + 1
            if seen[B[i]] == 2:
                count += 1

            arr.append(count)

        return arr