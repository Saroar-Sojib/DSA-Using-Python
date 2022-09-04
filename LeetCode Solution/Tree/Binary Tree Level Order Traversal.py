class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        res = []
        temp_list = []
        if not root:
            return res 
        temp_list.append(root)
        while temp_list:
            temp_len = len(temp_list)
            temp_res=[]
            for i in range(temp_len):
                node = temp_list.pop(0)
                temp_res.append(node.val)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            res.append(temp_res)
        return res 
    
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
    print(ans.levelOrder(Tree))