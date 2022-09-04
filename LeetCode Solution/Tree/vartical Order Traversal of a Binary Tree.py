# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        cols = defaultdict(lambda: defaultdict(list));
        
        q = [(root,0,0)]
        
        while q:
            temp = []
            
            for node, row, col in q:
                cols[col][row].append(node.val)
                if node.left:
                    temp.append((node.left, row+1, col-1))
                if node.right:
                    temp.append((node.right, row+1, col+1))
            q = temp
            
        ans = []
        for col in sorted(cols.keys()):
            temp = []
            for row in cols[col]:
                temp += sorted(cols[col][row])
            ans.append(temp)
        return ans

if __name__ == '__main__':
    '''
                4                          
              /   \  
            2      7 
           / \    / \ 
          1   3   6  9

    '''
    Tree = TreeNode(4)
    Tree.left = TreeNode(2)
    Tree.right = TreeNode(7)
    Tree.left.left = TreeNode(1)
    Tree.left.right = TreeNode(3)
    Tree.right.left = TreeNode(6)
    Tree.right.right = TreeNode(9)
    ans = Solution()
    print(ans.verticalTraversal(Tree))

        