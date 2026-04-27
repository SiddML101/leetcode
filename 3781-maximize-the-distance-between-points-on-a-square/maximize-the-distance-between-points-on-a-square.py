import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Step 1: Map 2D coordinates to 1D positions along the perimeter
        def get_1d_position(x, y):
            if y == 0: return x                     # Bottom edge
            if x == side: return side + y           # Right edge
            if y == side: return 2 * side + (side - x) # Top edge
            if x == 0: return 3 * side + (side - y)    # Left edge
            
        perimeter_len = 4 * side
        P = sorted([get_1d_position(x, y) for x, y in points])
        n = len(P)
        
        # Step 2: Double the array to easily handle circular wrap-around
        P_extended = P + [p + perimeter_len for p in P]
        
        # Helper to check if a distance 'd' is possible
        def can_place(d):
            # Try starting our selection from each of the original points
            for i in range(n):
                curr_idx = i
                count = 1
                
                # Try to pick k-1 more points
                for _ in range(k - 1):
                    # We need the next point to be at least 'd' distance away
                    target = P_extended[curr_idx] + d
                    curr_idx = bisect.bisect_left(P_extended, target)
                    
                    # If we run out of points, this starting position fails
                    if curr_idx >= len(P_extended):
                        break
                    count += 1
                
                # If we picked k points, check if the wrap-around distance is also >= d
                # The last point picked must be far enough from the first point (plus full perimeter)
                if count == k and P_extended[curr_idx] <= P_extended[i] + perimeter_len - d:
                    return True
                    
            return False

        # Step 3: Binary Search on the answer
        # The answer must be between 0 and `side` (since k >= 4)
        left = 0
        right = side
        best_dist = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                best_dist = mid
                left = mid + 1  # Try to find a larger minimum distance
            else:
                right = mid - 1 # Distance is too large, reduce it
                
        return best_dist