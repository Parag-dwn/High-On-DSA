# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 35 ms, faster than 94.55% of Python online submissions for Construct String from Binary Tree.
    # Memory Usage: 16.9 MB, less than 10.00% of Python online submissions for Construct String from Binary Tree.
    
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
        
            if root:
                if not root.left and root.right:
                    left = "()"
                else:
                    left = helper(root.left)
                    
                right = helper(root.right)

                return "("+str(root.val)+left+right+")"
            
            return ""
        
        return helper(root)[1:-1]
            
        
        
                