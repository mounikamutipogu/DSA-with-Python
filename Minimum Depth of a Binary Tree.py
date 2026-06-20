class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:# no root node
            return 0
        #if     
        if not root.left and not root.right:
            return 1
        #if left child does not exist
        if not root.left:
            return 1+self.minDepth(root.right)
        #if right child doesnot exit
        if not root.right:
            return 1+self.minDepth(root.left)
        #both child exits
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))