# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,min,max):
            if root is None: 
                return True
            if root.val <= min or root.val >= max:
                return False
            return isValid(root.left,min, root.val ) and isValid(root.right, root.val,max)
            return True
        
        return isValid(root,-float(inf), float(inf) )
    
def main():
    object = Solution()
    root = [2,1,3]
    print (object.isValidBST(root))


if __name__ == "__main__":
    main() 