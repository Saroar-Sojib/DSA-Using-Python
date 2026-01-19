# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_value):
            if not node:
                return 0
            res=0
            if node.val>=max_value:
                res+=1
                max_value=node.val
            res+=dfs(node.left,max_value)
            res+=dfs(node.right,max_value)
            return res 
        return dfs(root,float('-inf'))

if __name__ == '__main__':
    '''
                3                          
              /   \  
            9      20 
                   / \     
                  15   7   

    '''
    Tree = TreeNode(3)
    Tree.left = TreeNode(9)
    Tree.right = TreeNode(20)
    Tree.right.left = TreeNode(15)
    Tree.right.right = TreeNode(7)
    
    ans = Solution()
    print(ans.goodNodes(Tree))