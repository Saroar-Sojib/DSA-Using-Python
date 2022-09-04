class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        res = []
        if not root:
            return res 
        temp_list = []
        temp_list.append(root)
        while temp_list:
            right_side = None
            temp_len= len(temp_list)
            for i in range(temp_len):
                node = temp_list.pop(0)
                if node:
                    right_side = node 
                    temp_list.append(node.left)
                    temp_list.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res 
    
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
    print(ans.rightSideView(Tree))