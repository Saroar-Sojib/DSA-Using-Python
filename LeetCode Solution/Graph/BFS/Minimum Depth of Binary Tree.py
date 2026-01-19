class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        temp_list = []
        temp_list.append(root)
        cnt=1
        while temp_list:
            temp_len=len(temp_list)
            for i in range(temp_len):
                node = temp_list.pop(0)
                if node.left is None and node.right is None:
                    return cnt 
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            cnt+=1
        return cnt 
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
    print(ans.minDepth(Tree)) 