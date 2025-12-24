class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count = 0
        box_count = 0
        for i in range (len(apple)):
            count += apple[i]

        capacity.sort(reverse = True)
        for j in range (len(capacity)):
            if count > 0:
                count -= capacity[j]
                box_count += 1
            
        if count <= 0:
            return box_count
        else:
            return 0

        