class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
    
if __name__ == '__main__':
    '''
                4                          
              /   \  
            2      7 
           / \    / \ 
          1   3   6  9

                4                          
              /   \  
            2      7 
           / \    / \ 
          1   3   6  10

    '''
    Tree = TreeNode(4)
    Tree.left = TreeNode(2)
    Tree.right = TreeNode(7)
    Tree.left.left = TreeNode(1)
    Tree.left.right = TreeNode(3)
    Tree.right.left = TreeNode(6)
    Tree.right.right = TreeNode(9)
    Tree1 = TreeNode(4)
    Tree1.left = TreeNode(2)
    Tree1.right = TreeNode(7)
    Tree1.left.left = TreeNode(1)
    Tree1.left.right = TreeNode(3)
    Tree1.right.left = TreeNode(6)
    Tree1.right.right = TreeNode(10)
    ans = Solution()
    print(ans.isSameTree(Tree,Tree1))
