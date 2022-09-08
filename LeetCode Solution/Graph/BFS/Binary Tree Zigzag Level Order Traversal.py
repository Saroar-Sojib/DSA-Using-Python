class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res
        temp_list = []
        temp_list.append(root)
        side =1 
        while temp_list:
            temp_len = len(temp_list)
            level = []
            for i in range(temp_len):
                node = temp_list.pop(0)
                level.append(node.val)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            if side%2==0:
                level.reverse()
            res.append(level)
            side+=1
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
    print(ans.zigzagLevelOrder(Tree))  