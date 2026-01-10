class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = 0
        b = len(s) - 1
        temp = 0
        while a <= b:
            temp = s[a]
            s[a] = s[b]
            s[b] = temp
            a += 1
            b -= 1

        return s