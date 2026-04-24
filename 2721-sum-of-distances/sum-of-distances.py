class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices_map = defaultdict(list)

        for i, num in enumerate(nums):
            indices_map[num].append(i)

        arr = [0] * len(nums)

        for indices in indices_map.values():
            L = len(indices)

            if L == 1:
                continue

            current_sum = sum(indices) - L * indices[0]
            arr[indices[0]] = current_sum
            
            
            for k in range(1, L):
                
                diff = indices[k] - indices[k - 1]
                
                
                current_sum += diff * (2 * k - L)
                
                arr[indices[k]] = current_sum
                
        return arr
        