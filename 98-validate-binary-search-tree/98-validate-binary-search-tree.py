# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False
        self.prev = None
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.inorder(root)
        return self.flag
    
    def inorder(self, root: Optional[TreeNode]):
        #base condition
        
        if root is None:
            return False
        
        #inorder traversal 
        
        self.inorder(root.left)
        #st.pop()
        
        if self.prev != None and self.prev.val >= root.val:
            self.flag = False
        
        self.prev = root
        if self.flag:
            self.inorder(root.right)
            #st.pop()
        
        