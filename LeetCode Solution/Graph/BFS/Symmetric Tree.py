# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        left_side = []
        right_side = []
        left_side.append(root.left)
        right_side.append(root.right)
        while left_side and right_side:
            left_node=left_side.pop(0)
            right_node = right_side.pop(0)
            if left_node is None and right_node is None:
                continue 
            if left_node is None or right_node is None:
                return False 
            if left_node.val!=right_node.val:
                return False 
            left_side.append(left_node.left)
            right_side.append(right_node.right)
            
            left_side.append(left_node.right)
            right_side.append(right_node.left)
        return True

if __name__ == '__main__':
    '''
                4                          
              /   \  
            2      7 
           / \     
          1   3   
    '''
    Tree = TreeNode(4)
    Tree.left = TreeNode(2)
    Tree.right = TreeNode(7)
    Tree.left.left = TreeNode(1)
    Tree.left.right = TreeNode(3)
    ans = Solution()
    print(ans.isSymmetric(Tree)) 
        
            
            
        