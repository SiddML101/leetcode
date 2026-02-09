# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def Tree(root):
            if not root:
                return

            stack = [root]
            while stack:
                node = stack.pop()
                arr.append(node.val)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
        Tree(root)
        arr.sort()

        def build (l,r):
            if l > r:
                return

            m = (l+r)//2
            node = TreeNode(arr[m])
            node.left = build(l,m-1)
            node.right = build(m+1,r)
            return node

        return build(0,len(arr)-1)
        
       