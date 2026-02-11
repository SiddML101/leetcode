import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # --- Data Structures (Just Arrays) ---
        # size 4*n is standard for segment trees
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        # --- Helper Functions (Nested for speed) ---
        
        # Pushes lazy values down to children so we can read them later
        def push(node):
            if lazy[node] != 0:
                add_val = lazy[node]
                left_child = 2 * node
                right_child = 2 * node + 1
                
                # Update left child
                tree_min[left_child] += add_val
                tree_max[left_child] += add_val
                lazy[left_child] += add_val
                
                # Update right child
                tree_min[right_child] += add_val
                tree_max[right_child] += add_val
                lazy[right_child] += add_val
                
                # Clear current node's lazy
                lazy[node] = 0

        # Updates a range [l, r] with val
        def update(node, start, end, l, r, val):
            # No overlap
            if l > end or r < start:
                return
            
            # Total overlap
            if l <= start and end <= r:
                tree_min[node] += val
                tree_max[node] += val
                lazy[node] += val
                return
            
            # Partial overlap
            push(node)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            # Recalculate current node
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

        # Finds the LEFTMOST index where the value is 0
        def find_first_zero(node, start, end, limit_index):
            # If completely out of range
            if start > limit_index:
                return -1
            
            # Pruning: If 0 is impossible in this range (min > 0 or max < 0), skip it!
            # This is the line that makes it O(log N) instead of O(N)
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1
            
            # Leaf node found
            if start == end:
                return start if tree_min[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            # Try left child first (because we want the longest subarray -> smallest start index)
            res = find_first_zero(2 * node, start, mid, limit_index)
            if res != -1:
                return res
            
            # If not in left, try right
            return find_first_zero(2 * node + 1, mid + 1, end, limit_index)

        # --- Main Logic ---
        last_pos = {}
        max_len = 0
        
        for j in range(n):
            val = nums[j]
            
            # Even = +1, Odd = -1
            diff = 1 if val % 2 == 0 else -1
            
            # Find previous occurrence of this number
            # If never seen, prev is -1
            prev = last_pos.get(val, -1)
            
            # This number 'activates' the range just after its last appearance
            # Range Update: [prev + 1, j]
            update(1, 0, n - 1, prev + 1, j, diff)
            
            last_pos[val] = j
            
            # Efficiently query the tree for the first 0
            start_index = find_first_zero(1, 0, n - 1, j)
            
            if start_index != -1:
                current_len = j - start_index + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len
        