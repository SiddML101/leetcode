# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        lvl = 1
        max_lvl = 0
        
        queue = deque([root])
        while queue:
            lvl_size = len(queue)
            curr_sum = 0
            for _ in range (lvl_size):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_lvl = lvl

            lvl += 1

        return max_lvl


        